import requests
from pprint import pprint
from get_token import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes

url='http://localhost:3001/fotos'
mimetypes=MimeTypes()
# _print = print
# print = pprint

nome_arquivo='py.png'

mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]
print(mimetype_arquivo)


multipart = MultipartEncoder(
    fields={
        'aluno_id':'1',
        'foto':(nome_arquivo,open(nome_arquivo,'rb'),mimetype_arquivo)
        }
)
headers = {
    'Authorization':token,
    'Content-Type':multipart.content_type
}
response=requests.post(url=url,data=multipart,headers=headers)

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
    
