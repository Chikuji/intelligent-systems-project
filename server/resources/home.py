from flask_restful          import Resource

class HomePage(Resource):

    def get(self):

        return {"msg:": "If you're seeing this, it means the app is running!"}