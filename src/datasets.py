from model import Model

class GeneDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self, key="gene_symbol"):
        return super().get_unique_entries(key)
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, field: str, attribute: str):
        return super().get_sentences(field, attribute)
    
    def find_association(self, key: str, attribute: str, merged_model: Model, second_key:str = 'disease_name') -> list:
        return super().find_association(key, attribute, merged_model, second_key)


class DiseaseDataset(Model):
    def __init__(self, path:str) -> None:
        super().__init__(path)

    def get_unique_entries(self, key="disease_name"):
        return super().get_unique_entries(key)
    
    def most_frequent_association(self):
        return super().most_frequent_association()
    
    def get_sentences(self, key: str, attribute: str):
        return super().get_sentences(key, attribute)
    
    def find_association(self, key: str, attribute: str, merged_model:Model, second_key = 'gene_symbol') -> list:
        return super().find_association(key, attribute, merged_model, second_key)