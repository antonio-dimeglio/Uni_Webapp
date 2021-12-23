from model import Model
from os import getcwd
import pandas as pd


class GeneDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self, key="gene_symbol"):
        return super().get_unique_entries(key)
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, field: str, attribute: str):
        return super().get_sentences(field, attribute)
    
    def find_association(self, key: str, attribute: str, ds: Model, secondary_attribute:str) -> list:
        return super().find_association(key, attribute, ds)


class DiseaseDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self, key="disease_name"):
        return super().get_unique_entries(key)
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, key: str, attribute: str):
        return super().get_sentences(key, attribute)
    
    def find_association(self, key: str, attribute: str, merged_model:Model, secondary_attribute) -> list:
        return super().find_association(key, attribute, merged_model, secondary_attribute)


genes = GeneDataset(getcwd() + "/src/data/gene_evidences.tsv")
diseases = DiseaseDataset(getcwd() + "/src/data/disease_evidences.tsv") #keep in mind that the slashes are in the other direction if ran on windows
#print(genes.get_unique_entries())
#print(diseases.get_sentences(key="diseaseid", attribute="C0000737"))
#the merged model needs to be compiled beforehand in the controller
merged_model = pd.merge(genes.get_dataframe(), diseases.get_dataframe(), "inner", "pmid")
print(diseases.find_association("diseaseid", "C000656484", merged_model, "gene_symbol"))

    
