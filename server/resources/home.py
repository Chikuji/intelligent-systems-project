from flask_restful          import Resource

class HomePage(Resource):

    def get(self):

        return {"msg:": "app is running!"}