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
    def __init__(self, path:str) -> None:
        self.__path = path
        self.__load_dataset()


    #Methods
    def get_unique_entries(self, key:str) -> list:
        if (key in self.__labels):
            unique_values = np.sort(self.__dataframe[key].unique())
            return unique_values
        
        return []

    def most_frequent_association(self): 
        '''
        TODO
        '''
        pass

    def get_sentences(self, key:str, attribute:str) -> list:
        if (key in self.__labels):
            if (attribute in self.get_unique_entries(key)):
                sentences = self.__dataframe[self.__dataframe[key] == attribute]["sentence"]
                return sentences.tolist()


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
                

        return None