# Server
This folder contains all code from the second part of the project developed in the course _Development of Intelligent Computer Systems_ at IME-USP.

The API developed was deployed in the cloud using Heroku, you can access here (bellow you can find more details about the endpoints):

- https://categorization-api.herokuapp.com/home
- https://categorization-api.herokuapp.com/v1/categorize
- https://categorization-api.herokuapp.com/v1/test-request

_note: sometimes it make take a while to load since it was deployed in a free plan, so, the app 'sleeps' if it's not receiving rquests_

## Endpoints:
1) `/home` (GET): returns a simple json just to check if the app is able of receiving requests;

2) `/v1/categorize` (POST): receives a json in the following format and returns the category for each product:

```json
{
  "products": [
    {
      "title": "Lembrancinha",
      "query": "lembrancinhas",
      "concatenated_tags":"lembrancinhas"
    },
    {
      "title": "Carrinho de Bebê",
      "query": "Carrinho de Bebê",
      "concatenated_tags":"Carrinho de Bebê"
    }
  ]
}
```

We can send a json request to it by navegating into the `data` folder in the terminal and type the following command:

```bash
curl --header "Content-Type: application/json"   --request POST   --data @json_request.json   http://localhost:5000/v1/categorize
```

This json structure allows the API to receive how many products we need. For sending many products at once, just add the fields. For something like straming, just send how many request you would want with just one product.

If you send a field with empty

2) `/v1/test-request` (GET): used to test if the app is able of making predictions. When this endpoint receives a GET request, it automatically loads [this json file][1] and return the category for all products in the file.



[1]: https://github.com/Chikuji/intelligent-systems-project/blob/main/server/data/json_request.json
