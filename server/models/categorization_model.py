from http.client import BAD_REQUEST
from flask_restful import reqparse

from tools.preparation_tools import PreparationTools
from tools.prediction_tools import PredictionTools

class CategorizationModel():

    def __init__ (self):

        self.text_preparation_tools = PreparationTools()

        self.categorizer = PredictionTools()
    

    def predict(self, product):
        """
        Receives a dictionary containing title, query, and/or concatenated_tags about a product
        and returns its category
        
        :param data: a dictionary.
        
        :returns: a str with the product's category."""

        pred_cols = ['title', 'query', 'concatenated_tags']

        product_keys = product.keys()

        conditions = ['title' not in product_keys, 'query' not in product_keys, 'concatenated_tags' not in product_keys]

        if all(conditions):

            return None
        
        conditions = [not product.get('title'), not product.get('query'), not product.get('concatenated_tags')]
        
        # if all columns contains None or empty string, we'll return a None, since we can't predict
        ## Also, in order to don't stop processing the whole data passed, we return this None value
        if all(conditions):

            return None

        # adding empty string to avoid indexing error
        for col in pred_cols:
                if col not in product_keys:
                    product[col] = ""

        # Filling Missing Values
        for key in product.keys():
            if not product[key]:
                product[key] = self.text_preparation_tools.filling_NAs()

        # As the same we did when training. we'll create our prediction feature by concatenating
        ## those three columns and removing the stopwords
        product = self.text_preparation_tools.create_text_feature(product)
        
        # Categorizing Product
        product_category = self.categorizer.categorize_product(product)


        return product_category


    def data_validation(self, data):
        """
        Receives a dictionary object and check if the data is in the required format..
        
        :param data: a dictionary.
        
        :returns: True if the data is in a wrong format and False if it's Ok."""
        
        # this is not the best way to do it, since we need a lot of code to track all conditions.
        ## But for simplicity, decided to do this way

        # receiving something other than product
        if not ('products' in data.keys() and len(data.keys()) == 1):
            
            return True
        
        # not list
        if not isinstance(data['products'], list):
            
            return True

        # empty
        if not data['products']:

            return True
        
        # not dict on product list
        if not all(isinstance(d, dict) for d in data['products']):
            
            return True
    

        return False
