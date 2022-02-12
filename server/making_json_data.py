import json

import pandas as pd


df_test = pd.read_csv('../data/test_products.csv')

df_test = df_test[['query', 'title', 'concatenated_tags']]

df_test = df_test.to_json(orient='records', force_ascii=False)

product_list_json = json.loads(df_test)

with open('data/json_request.json', 'w') as f:
    json.dump({'products': product_list_json}, f)