import pickle

import pandas as pd

from instances.config import MODEL_PATH


class PredictionTools():

    def __init__(self):

        self.categorization_model = pickle.load(open(MODEL_PATH, 'rb'))

    def categorize_product(self, product):

        print('dados ppara predição ', product)

        predicted_category = self.categorization_model.predict(pd.Series(product))

        return predicted_category[0]

