from flask                       import request
from flask_restful               import Resource
from models.categorization_model import CategorizationModel


categorizationModel_ = CategorizationModel()

class Categorization(Resource):


    def get(self):

        return {"msg": "You've sent a GET request to this endpoint. For making categorization requests, please, send a POST with the right json format or try the request testing endpoint: v1/test-request"}

    def post(self):
        
        # products = Categorization.parser.parse_args()
        products = request.json
        print(products)

        if categorizationModel_.data_validation(products):
            
            return {"message": {
                        "products": "Field 'products' as a list of dictionaries is required!!"
                    }
                }, 400


        try:

            categories = [categorizationModel_.predict(product) for product in products['products']]

        except Exception as e:

            return {'message': 'Error while categorizing product: '+ str(e)}, 500

        
        return {

            "categories": categories
            
            }, 200