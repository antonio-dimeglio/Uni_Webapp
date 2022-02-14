#more detailed documentation can be found in the text file

from flask import Flask, render_template, request
from os import getcwd
import platform

import pandas as pd
from datasets import GeneDataset, DiseaseDataset
from model import Model


'''
At first the getcwd() method from the os module is used to get the current working directory
Then using the platform.system method we retreive the current OS used to set the correct
format to load the datasets
'''
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
    '''Depending on the selection made beforehand on the dataset to visualise
    different attributes are set so that they can then get passed to the jinja template engine
    to render them onto the page
    '''
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

@app.route("/results/<operation>", methods=['POST'])
def results(operation:str):
    '''
    Based on the query requested the result is obtained, in the case of the geneid it is a numeric value
    hence the try except block is used to type cast the input value of the query, otherwise the value 
    gets treated as a string and no output is obtained.
    '''
    if request.form['Selection'] == 'geneid':
        try:
            attribute = int(request.form['user_request'])
        except:
            attribute=None  
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


'''
The app.run() method is used to launch the webserve while the two assignments before they are 
set to True as they were used to automatically update the template during debugging
'''
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run()
