#more detailed documentation can be found in the text file

from __future__ import annotations
import pandas as pd
import numpy as np
from pandas.core.reshape.merge import merge
'''The __future__ module is imported to allow better typinting'''

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
    #get_labels method returns a set containing the labels of the dataframe
    def get_labels(self) -> set: return set(self.__dataframe.columns) 

    #get_dataframe method returns the Pandas dataframe of the models
    def get_dataframe(self): return self.__dataframe
    
    #get_path returns the path of dataframe files as a string
    def get_path(self): return self.__path
  
    #get_shape returns the shape of the model as a tuple with format (row, col)  
    def get_shape(self): return self.__dataframe.shape

    #Constructor
    def __init__(self, path:str = "", is_dataframe:bool = False, df:pd.DataFrame = None) -> None:
        '''As python does not support constructor overloading the is_dataframe flag is used to
        understand if a pandas dataframe is passed directly or if it should be loaded using the 
        __load_dataset() method'''
        if (is_dataframe == True and type(df) == pd.DataFrame):
            self.__dataframe = df
            self.__labels = set(df.columns)
            self.__path = ""
        else:
            self.__path = path
            self.__load_dataset()


    #Methods

    def get_unique_entries(self, key:str) -> list:
        '''after a check on the key passed all the values for that key are retreived, all the values
        are selected once in order to not have repetitions and then they are sorted in ascending order
        using numpy; if the key is incorrect  an empty list is returned'''
        if (key in self.__labels):
            unique_values = np.sort(self.__dataframe[key].unique()) 
            return unique_values
        
        return []

    def get_sentences(self, key:str, attribute:str) -> list:
        '''given valid key and attribute (such as Gene Id, Gene Symbol, Disease name, Disease ID ) this 
        method returns all the sentences related to that attribute as a list. If the key or the attribute
        is invalid None is returned'''
        if (key in self.__labels):
            if (attribute in self.get_unique_entries(key)):
                sentences = self.__dataframe[self.__dataframe[key] == attribute]["sentence"]
                return sentences.tolist()

        print("Failed to retreive the sentences, are you sure that the function arguments are correct?")
        return None


    def __load_dataset(self):
        '''This function is used to load a tsv dataset as a pandas dataframe.
        If a FileNotFoundError exception is raised the dataframe is set to None 
        and an error prompt is printed'''
        print(f"Loading dataset: {self.__path}")
        try:
            self.__dataframe = pd.read_csv(self.__path, header=0, sep='\t')
            self.__labels = set(self.__dataframe.columns)
            print("Dataset loaded.")
        except FileNotFoundError:
            self.__dataframe = None
            print("Dataset not found, check the inserted path!")
        
    def find_association(self, key:str, attribute:str, merged_model:Model, second_key:str) -> list:
        '''Given the element of a column the function returns a list of associated attributes of 
        another column. Firstly, we check if the key belongs to the labels, if this condition is 
        True we check if the attribute belongs to the list returned by the get_unique_entries(key)
        method. If the condition is True the function creates a set with all the elements of the 
        second_key column that are associated with the elements of the first key.
	    If one of the conditions is not satisfied the function returns None and an error prompt is printed.'''
        if (key in self.__labels) and (second_key in merged_model.get_labels()):
            if (attribute in self.get_unique_entries(key)):
                
                associations = merged_model.get_dataframe()[merged_model.get_dataframe()[key] == attribute][second_key]
                return list(associations)
            else:
                return None
        
        print("Failed to retreive associations, are you sure that the function arguments are correct?")
        return None

    #Static methods

    @staticmethod
    def merge_models(m1:Model, m2:Model, on_key:str):
        '''The method is able to merge two dataframes utilizing a common element, a first check makes
        sure that the key is valid (belongs to both models). The function returns an instance of the class 
        Model where the flag is_dataframe=True and the attribute df is the newly created merged DataFrame.'''
        print("Trying to merge the datasets...")
        if (on_key in m1.get_labels() and on_key in m2.get_labels()):
            merged_model = pd.merge(m1.get_dataframe(), m2.get_dataframe(), "inner", on=on_key)
            print("Merge successful.")
            return Model(is_dataframe=True, df = merged_model)
        
        print("Failed to merge the datasets: are you sure the function arguments are correct?")
        return None

    @staticmethod
    def most_frequent_association(merged_model:Model, key:list=['gene_symbol', 'disease_name'], n:int = 10) -> list: 
        '''The method provides the 10 top most frequent associations between the two DataFrames Genes and 
        Disease, it returns associations as a list'''
        most_frequent_ids = merged_model.get_dataframe()[key].value_counts()[:n].index.tolist()
        return most_frequent_ids