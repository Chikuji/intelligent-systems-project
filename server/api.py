from flask import Flask

api = Flask(__name__)

@api.route("/v1/categorize", methods=["GET"])
def hello():
    return { "messagem" : "Hello, Felipe"}


