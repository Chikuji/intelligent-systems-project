from flask                       import request
from flask_restful               import Resource
from models.categorization_model import CategorizationModel


categorizationModel_ = CategorizationModel()

class Categorization(Resource):

    parser = categorizationModel_.classificationParser()

    def post(self):
        
        products = Categorization.parser.parse_args()


        try:

            categories = [categorizationModel_.predict(product) for product in products['products']]

        except Exception as e:

            return {'message': 'Error while categorizing product: '+ str(e)}, 500

        
        return {

            "categories": categories
            
            }, 200