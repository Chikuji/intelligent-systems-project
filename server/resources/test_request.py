import json
from flask_restful          import Resource
from models.categorization_model import CategorizationModel

from instances.config import JSON_TEST

categorizationModel_ = CategorizationModel()


class TestRequest(Resource):

    parser = categorizationModel_.classificationParser()

    def get(self):

        with open(JSON_TEST, 'rb') as f:
            products = json.load(f)

        try:

            categories = [categorizationModel_.predict(product) for product in products['products']]

        except Exception as e:

            return {'message': 'Error while categorizing product: '+ str(e)}, 500

        
        return {

            "categories": categories
            
            }, 200