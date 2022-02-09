from flask import Flask, render_template, request
from os import getcwd
import platform

import pandas as pd
from datasets import GeneDataset, DiseaseDataset
from model import Model


#We check for the system current os to use the correct path format
genes_path = disease_path = getcwd()

if (platform.system() == 'Windows'):
    genes_path += "\\data\\gene_evidences.tsv"
    disease_path += "\\data\\disease_evidences.tsv"
else:
    genes_path += "/data/gene_evidences.tsv"
    disease_path += "/data/disease_evidences.tsv"


#The dataset objects are created
genes = GeneDataset(genes_path)
diseases = DiseaseDataset(disease_path)
merged_model = Model.merge_models(genes, diseases, "pmid")


#A flask app object is created
app = Flask(__name__)

#Homepage route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/data/<datatype>")
def data_managment(datatype: str):
    gene_operation_description = [
        "Obtain a list of different genes detected in literature",'''Given a gene symbol or
        its ID, this function will provide the list of sentences that are an evidence in literature
        about the relation of this gene with COVID-19''', "Find the 10 most frequent association between genes and disease", 
        "given a gene symbol or its ID, this function will provide the list of diseases such a gene is associated with"
    ]

    gene_operation = ['genes_list', 'list_of_sentence_gene', 'most_frequent_association', 'list_of_disease']

    disease_operation_description = [
        "Obtain a list of different disease detected in literature",'''Given a disease_name or
        its ID, this function will provide the list of sentences that are an evidence in literature
        about the relation of this disease with COVID-19''', "Find the 10 most frequent association between genes and disease", 
        "given a disease_name or its ID, this function will provide the list of genes such a disease is associated with"
    ]

    disease_operation = ['disease_list', 'list_of_sentence_disease', 'most_frequent_association', 'list_of_gene']
    if datatype == 'gene':
        shape = genes.get_shape()
        labels = genes.get_labels()
        operations = gene_operation
        descriptions = gene_operation_description
    else:
        shape = diseases.get_shape()
        labels = diseases.get_labels()
        operations = disease_operation
        descriptions = disease_operation_description

    return render_template("data.html", datatype=datatype, length = len(operation), shape = shape, labels = labels, operations = operations, operation_description=descriptions)

@app.route("/results/<operation>", methods=['GET', 'POST'])
def results(operation:str):
    if request.method == "GET":
        if operation == 'genes_list':
            result = genes.get_unique_entries()
        if operation == 'most_frequent_association':
            result = Model.most_frequent_association(merged_model=merged_model)
    else:
        print('OPERAZIONE: ', operation)
        if operation == 'list_of_sentence_gene':
            print(request.form.listvalues())
            result = genes.get_sentences(request.form['Selection'], request.form['user_request'])

    return render_template("results.html", result=result, result_type = operation)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run()
