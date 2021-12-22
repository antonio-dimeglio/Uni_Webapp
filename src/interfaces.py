from abc import ABC, abstractmethod

class Dataset(ABC):
    '''
    The Dataset class is an interface that provides the method that both datasets object will need to use
    '''
    @abstractmethod
    def load_data():
        '''
        This method is used to load data and checks if the dataset is actually present in the project folder    
        '''
        pass

    @abstractmethod
    def get_columns():
        '''
        This method returns a tuple containing all the attributes of the dataset
        '''
        pass

    @abstractmethod
    def get_shape():
        '''
        This method returns the shape of the dataset using a tuple such as (rows, columns)
        '''
        pass

    @abstractmethod
    def inner_join():
        '''
        This method executes an inner join based on the first and second attributes passed

        '''
        pass

    @abstractmethod
    def get_unique_list():
        '''
        Returns a list of unique elements for a given column
        '''
        pass
