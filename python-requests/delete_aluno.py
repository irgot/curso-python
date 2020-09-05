import requests
from pprint import pprint
from get_token import token

_print=print
print=pprint

url='http://localhost:3001/alunos/2'

headers={
     'Authorization':token
}


response = requests.delete(url,headers=headers)

if response.status_code>=200 and response.status_code<=299:
    print(response.status_code)
    print(response.reason)
    response_data=response.json()
    print(response_data)
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
