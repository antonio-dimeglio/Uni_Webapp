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