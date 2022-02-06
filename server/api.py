from flask import Flask
from flask import request
import os
import pickle


# path variables

MODEL_PATH    = os.environ['MODEL_PATH']

# Carregando a Máquina Preditiva
pickle_in = open(MODEL_PATH, 'rb')

ml_model = pickle.load(pickle_in)


api = Flask(__name__)

@api.route("/hello/<name>", methods=["GET"])
def hello(name):
    return { "messagem" : f"Hello, {name}"}


@api.route("/bye", methods=["POST"])
def bye():
    title = request.json["title"],
    query = request.json["query"],
    concatenated_tags = request.json["concatenated_tags"]

    concat = str(title) + " " + str(query) + " " + str(concatenated_tags)

    resut = ml_model.predict([concat])

    return { "categories" : f"{resut}"}

