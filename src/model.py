from __future__ import annotations
import pandas as pd
import numpy as np
from pandas.core.reshape.merge import merge

class Model():
    '''
    This class is used as a base class for both dataset classes
    The view that can be applied are agnostic and need some checking/input
    sanitization to avoid server crashes. 
    '''

    #Getter and Setter
    '''
    These values are set only once as the Model object is created, hence no setter is needed
    '''
    def get_labels(self) -> list: return list(self.__dataframe)

    def get_dataframe(self): return self.__dataframe

    def get_path(self): return self.__path

    #Constructor
    def __init__(self, path:str = "", is_dataframe:bool = False, df:pd.DataFrame = None) -> None:
        if (is_dataframe):
            self.__dataframe = df
            self.__labels = set(df.columns)
        else:
            self.__path = path
            self.__load_dataset()


    #Methods
    def get_unique_entries(self, key:str) -> list:
        if (key in self.__labels):
            unique_values = np.sort(self.__dataframe[key].unique())
            return unique_values
        
        return []

    def get_sentences(self, key:str, attribute:str) -> list:
        if (key in self.__labels):
            if (attribute in self.get_unique_entries(key)):
                sentences = self.__dataframe[self.__dataframe[key] == attribute]["sentence"]
                return sentences.tolist()

        print("Failed to retreive the sentences, are you sure that the function arguments are correct?")
        return []

    def get_shape(self): 
        return self.__dataframe.shape

    def __load_dataset(self):
        print(f"Loading dataset: {self.__path}")
        try:
            self.__dataframe = pd.read_csv(self.__path, header=0, sep='\t')
            self.__labels = set(self.__dataframe.columns)
            print("Dataset loaded.")
        except FileNotFoundError:
            self.__dataframe = None
            print("Dataset not found, check the inserted path!")
        
    def find_association(self, key:str, attribute:str, merged_model:Model, second_attribute:str) -> list:
        if (key in self.__labels):
            if (attribute in self.get_unique_entries(key)):
                associations = merged_model[merged_model[key] == attribute][second_attribute]
                return associations
        
        print("Failed to retreive associations, are you sure that the function arguments are correct?")
        return None

    #Static methods

    @staticmethod
    def merge_models(m1:Model, m2:Model, on_key:str):
        print("Trying to merge the datasets...")
        if (on_key in m1.get_labels() and on_key in m2.get_labels()):
            merged_model = pd.merge(m1.get_dataframe(), m2.get_dataframe(), "inner", on=on_key)
            print("Merge successful.")
            return Model(is_dataframe=True, df = merged_model)
        
        print("Failed to merge the datasets: are you sure the function arguments are correct?")
        return None

    @staticmethod
    def most_frequent_association(merged_model:Model, key:str="pmid", n:int = 10): 
        most_frequent_ids = merged_model.__dataframe[key].value_counts()[:n].index.tolist()
        return most_frequent_ids
