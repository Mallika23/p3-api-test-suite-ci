import os
import requests


url = "https://reqres.in/api/users"
#Authentication using API key
headers = {
    'x-api-key': os.environ['REQRES_API_KEY']
}
#GET
response = requests.get(url, headers=headers)
response.raise_for_status()
print("GET Response:")
print(response.json())


#POST
payload = {'id': 123,'email': 'malv.malv@reqres.in', 'first_name': 'Mallika', 'last_name': 'Verma', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
print("POST Response:")
print(response.json())
#GET after POST
response = requests.get(url, headers=headers)
response.raise_for_status()
print("GET Response after POST:")
print(response.json())

#PUT ENDPOINT IS NOT SAME AS GET AND POST
url = "https://reqres.in/api/users/2"
#PUT
param = {'id': 7}
payload = {'first_name': 'Rohit', 'last_name': 'Sharma'}
response = requests.put(url, headers=headers, json=payload)
response.raise_for_status()
print("PUT Response:")
print(response.json())
#GET after PUT
response = requests.get(url, headers=headers)
response.raise_for_status()
print("GET Response after PUT:")
print(response.json())

#DELETE
param = {'id': 123}
response = requests.delete(url, headers=headers, params=param)  
response.raise_for_status()
print("DELETE Response:")
print(response.status_code)
#GET after DELETE
response = requests.get(url, headers=headers)
response.raise_for_status()
print("GET Response after DELETE:")
print(response.json())
