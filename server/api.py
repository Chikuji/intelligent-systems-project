from flask                      import Flask
from flask                      import request
from flask_restful              import Api

from resources.home           import HomePage
from resources.test_request   import TestRequest
from resources.categorization import Categorization

print('Starting API...')


app = Flask(__name__)

api = Api(app)

api.add_resource(HomePage, '/home')
api.add_resource(TestRequest, '/v1/test-request')
api.add_resource(Categorization, '/v1/categorize')