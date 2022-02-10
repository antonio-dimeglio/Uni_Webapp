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

    associations = Model.most_frequent_association(merged_model)
    if datatype == 'gene':
        shape = genes.get_shape()
        labels = genes.get_labels()
        dataset_name = 'gene_evidences.tsv'
        entry = genes.get_unique_entries()
    else:
        shape = diseases.get_shape()
        labels = diseases.get_labels()
        dataset_name = 'disease_evidences.tsv'
        entry = diseases.get_unique_entries()

    return render_template("data.html", datatype=datatype, associations = associations, shape = shape, labels = labels, dataset_name=dataset_name, entry=entry)

@app.route("/results/<operation>", methods=['GET', 'POST'])
def results(operation:str):
    print(request.form.listvalues())
    if request.form['Selection'] == 'geneid':
        attribute = int(request.form['user_request'])
    else:
        attribute = request.form['user_request']

    if operation == 'list_of_sentence_gene' or operation == 'list_of_sentence_disease':
        if operation == 'list_of_sentence_gene':
            result = genes.get_sentences(request.form['Selection'], attribute)
        else:
            result = diseases.get_sentences(request.form['Selection'], attribute)

    elif operation == 'list_of_disease' or operation == 'list_of_genes':
        if operation == 'list_of_disease':
            result = genes.find_association(request.form['Selection'], attribute, merged_model)
        else:
            result = diseases.find_association(request.form['Selection'], attribute, merged_model)

    return render_template("results.html", result=result, result_type = operation)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run()
