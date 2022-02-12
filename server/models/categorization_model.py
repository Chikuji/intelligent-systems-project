from http.client import BAD_REQUEST
from flask_restful import reqparse

from tools.preparation_tools import PreparationTools
from tools.prediction_tools import PredictionTools

class CategorizationModel():

    def __init__ (self):

        self.text_preparation_tools = PreparationTools()

        self.categorizer = PredictionTools()
    

    def predict(self, product):

        conditions = [not product['title'], not product['query'], not product['concatenated_tags']]
        
        # if all columns contains None or empty string, we'll return a None, since we can't predict
        ## Also, in order to don't stop processing the whole data passed, we return this None value
        if any(conditions):

            return None

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


    def classificationParser(self):

        parser = reqparse.RequestParser()

        parser.add_argument('products',

            required=True,

            type=dict, action='append',

            help = f"Field 'products' as list of dictionaries is required!!")


        return parser
