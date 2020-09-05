import requests
from pprint import pprint
url='http://localhost:3001/users'
_print = pprint


user_data = {
    "nome": "Igor Souza",
    "password": "f123f123bb",
    "email": "igor.ferreira.souza@gmail.com"
}


response=requests.post(url=url,json=user_data)

if response.status_code>=200 and response.status_code<=299:
    #Sucesso
    print('Status Code',response.status_code)
    print('Reason',response.reason)
    # print('Texto',response.text)
    print('Json',response.json())
else:
    print('Status Code',response.status_code)
    print('Reason',response.reason)
    print('Texto',response.text)
    # print('Json',response.json())
    
