import os
import requests
import pytest


#Here since we are using external API we dont need to write main.py coz that is to CREATE an API
# to create a new local API we can use FastAPI()

url = "https://reqres.in/api/users"
#Authentication using API key
headers = {
    
    'x-api-key': os.environ['REQRES_API_KEY'] 
}

@pytest.fixture(autouse=True)
def clear_todo_items():
    print("provide a fresh instance of class and cleans up after the test completes")
    yield   

def test_get_users():
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("GET Response:")
    print(response.json())
    assert response.status_code == 200
    assert "data" in response.json()

def test_post_user():
    payload = {'id': 123,'email': 'test@example.com'}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    assert response.status_code == 201
    assert response.json()['id'] == 123

def test_put_user():
    url_put = "https://reqres.in/api/users/2"
    payload = {'first_name': 'Rohit', 'last_name': 'Sharma'}
    response = requests.put(url_put, headers=headers, json=payload)
    response.raise_for_status()
    assert response.status_code == 200
    assert response.json()['first_name'] == 'Rohit'
    assert response.json()['last_name'] == 'Sharma'

def test_delete_user():
    url_delete = "https://reqres.in/api/users/2"
    response = requests.delete(url_delete, headers=headers)
    response.raise_for_status()
    assert response.status_code == 204

    

# def test_get_after_delete():
#     url_get = "https://reqres.in/api/users/2"
#     response = requests.get(url_get, headers=headers)
#     assert response.status_code == 404

def test_get_after_post():
    payload = {'id': 123,'email': 'test @example.com'}
    response_post = requests.post(url, headers=headers, json=payload) 
    assert response_post.status_code == 201
    assert response_post.json()['id'] == 123

def test_get_after_put():
    url_put = "https://reqres.in/api/users/2"
    payload = {'first_name': 'Rohit', 'last_name': 'Sharma'}
    response_put = requests.put(url_put, headers=headers, json=payload)
    assert response_put.status_code == 200
    assert response_put.json()['first_name'] == 'Rohit'
    assert response_put.json()['last_name'] == 'Sharma'

def test_negative_get_user():
    url_invalid = "https://reqres.in/api/users/2"
    response = requests.get(url_invalid)
    assert response.status_code == 401      #unauthorized since we are not passing the headers with API key

def test_negative_post_user():
    url_invalid = "https://reqres.in/api/login/"
    payload = {'id': '123','first_name': '123'}
    response = requests.post(url_invalid, headers=headers, json=payload)
    assert response.status_code == 400

def test_negative_put_user():
    url_put = "https://reqres.in/api/register"
    payload = {'email': 'sydney@fife'}
    response = requests.put(url_put, headers=headers, json=payload)
    assert response.status_code == 404

def test_negative_delete_user():
    url_delete = "https://reqres.in"
    param = {'id': 123}
    response = requests.delete(url_delete, headers=headers, params=param)  
    assert response.status_code == 404

# parameterized test for POST endpoint with different payloads and expected results
@pytest.mark.parametrize("payload, expected_id, expected_status", [
    ({'id': 123,'email': 'test@example.com'}, 123, 201),
    ({'id': 456,'email': 'tst@example.com'}, 456, 201),
    ({'id': 789,'email': 'test2@example.com'}, 789, 201)
])
def test_post_user_params(payload, expected_id, expected_status):
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    assert response.status_code == expected_status
    assert response.json()['id'] == expected_id


