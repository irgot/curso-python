import requests
from pprint import pprint
url='http://localhost:3001/tokens'
_print = pprint


user_data = {
    "email": "igor.ferreira.souza@gmail.com",
    "password": "f123f123bb",    
}


response=requests.post(url=url,json=user_data)

if response.status_code>=200 and response.status_code<=299:
    #Sucesso
    print('Status Code',response.status_code)
    print('Reason',response.reason)
    # print('Texto',response.text)
    response_data = response.json()
    token=response_data['token']

    with open ('token.txt','w') as file:
        file.write(token)
else:
    print('Status Code',response.status_code)
    print('Reason',response.reason)
    print('Texto',response.text)
    # print('Json',response.json())
    
