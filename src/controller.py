from flask import Flask, render_template
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
merged_dataframe = Model.merge_models(genes, diseases, "pmid")

'''
#A flask app object is created
app = Flask(__name__)


#Homepage route
@app.route("/")
def home():
    return render_template("layout.html")


app.run()
'''