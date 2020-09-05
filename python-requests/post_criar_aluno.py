import requests
from pprint import pprint
from get_token import token

url='http://localhost:3001/alunos'
headers = {
    'Authorization':token
}

_print = pprint


aluno_data = {
    "nome":"Luana",
    "sobrenome":"Santos",
    "email":"luana.santos@ricoy.com.br",
    "idade":"36",
    "peso":"90.03",
    "altura": "1.90"
}


response=requests.post(url=url,json=aluno_data,headers=headers)

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
    
