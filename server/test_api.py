import json
import pytest
import requests

endpoint = 'http://localhost:5000/v1/categorize'

def make_request(json_input):
	global endpoint
	return requests.post(endpoint, json=json_input)


@pytest.mark.parametrize("input", [
        {"products": None},
        {"products": ""},
        {"products": 2},
        {"products": {}},
        {"products": []},
        {"products": [], "products2": []}
    ])
def test_invalid_data(input):
    response = make_request(input)

    assert response.status_code == 400
    
@pytest.mark.parametrize("input", [
        {"products": [{"test": ""}]}
    ])
    
def test_inexistence_features(input):
    response = make_request(input)

    assert response.status_code == 200


@pytest.mark.parametrize("input", [
        {"products": [{"test": "","query": "Lembrancinha","title": "Lembrancinha", "concatenated_tags": "Lembrancinha"}]},
        {"products": [{"title": "Lembrancinha"}]}])
    
def test_running_ok(input):
    response = make_request(input)

    assert response.status_code == 200
    
@pytest.mark.parametrize("input", [
        {"products": [{"query": "","title": "", "concatenated_tags": ""}]}
        
        ])
    
def test_all_NA(input):
    response = make_request(input)

    assert response.status_code == 200
    assert json.loads(response.text)["categories"][0] == None
    
@pytest.mark.parametrize("input", [
        {"products": [{"query": "","title": "", "concatenated_tags": ""}]}
        
        ])
    
def test_return_length(input):
    response = make_request(input)

    assert len(json.loads(response.text)["categories"]) == len(input['products'])
