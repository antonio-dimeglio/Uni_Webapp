from model import Model
from os import getcwd


class GeneDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self):
        return super().get_unique_entries("gene_symbol")
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, field: str, attribute: str):
        return super().get_sentences(field, attribute)
    
    def find_association(self, key: str, attribute: str) -> list:
        return super().find_association(key, attribute)


class DiseaseDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self):
        return super().get_unique_entries("disease_name")
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, key: str, attribute: str):
        return super().get_sentences(key, attribute)
    
    def find_association(self, key: str, attribute: str) -> list:
        return super().find_association(key, attribute)


#genes = GeneDataset(getcwd() + "/src/data/gene_evidences.tsv")
diseases = DiseaseDataset(getcwd() + "\\data\\disease_evidences.tsv") #keep in mind that the slashes are in the other direction if ran on windows
#print(genes.get_unique_entries())
#print(diseases.get_sentences("gene_symbol", ""))
print(diseases.find_association(key="diseaseid", attribute="C0000737"))