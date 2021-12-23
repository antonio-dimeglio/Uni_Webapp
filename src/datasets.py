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


class DiseaseDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self):
        return super().get_unique_entries("disease_name")
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, id: str):
        return super().get_sentences(id)


genes = GeneDataset(getcwd() + "/src/data/gene_evidences.tsv")
#diseases = DiseaseDataset(getcwd() + "/src/data/disease_evidences.tsv")
#print(genes.get_unique_entries())
print(genes.get_sentences("gene_symbol", ""))