def desafio72():
    numeros=('zero','um','dois','três','quatro'
    ,'cinco','seis','sete','oito','nove','dez',
    'onze','doze','treze','quatorze','quize',
    'desesseis','desessete','desoito','desenove','vinte')
    n1=-1
    while(n1 not in range(1,21)):
        n1=int(input('Digite um número entre 1 e 20: '))
    print(f'O número digitado foi {numeros[n1]}')

def desafio73():
    brasileirao=('internacional','atletico-mg','são paulo','vasco','flamengo',
    'palmeiras','santos','fluminense','ceará','fortaleza',
    'atlético-go','grêmio','athlético-pr','sport','corinthians','bahia','botafogo',
    'goiás','coritiba','bragantino')

    print(f'Os cinco primeiros colocados são: {brasileirao[:5]}')
    print(f'Os 4 ultimos colocados são:{brasileirao[-4:]}')
    print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
    print(f'O time do corinthians está na posição: {brasileirao.index("corinthians")+1}')
    pass

def desafio74():
    from random import randint
    n1 = randint(1,60)
    n2 = randint(1,60)
    n3 = randint(1,60)
    n4 = randint(1,60)
    n5 = randint(1,60)    
    maior = 0
    menor = 0
    numeros=(n1,n2,n3,n4,n5)
    print(f'Os números gerados foram:{numeros}')
    for i,n in enumerate(numeros):        
        if i==0:
            menor=n
            maior=n
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    print(f'O menor número sorteado foi: {menor} e o maior foi {maior}.')

def desafio75():
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))
    n4 = int(input('Digite o 4º número: '))
    
    numeros=(n1,n2,n3,n4)
    print(f'O número 9 apareceu: {numeros.count(9)} vezes.')
    try:
        posicao = numeros.index(3)
        print(f'O número 3 apareceu na {posicao}ª posição.')
    except ValueError as e:
        posicao = -1
        print(f'O número 3 não foi encontrado nos valores digitados.')
        pass
    print('Os números pares são: ',end='')
    for numero in numeros:
        print(f'{numero} ' if numero%2==0 else '',end='')
    print('\n FIM!! ')
    


def desafio76():
    produtos = ('Pão', 0.56,'Leite', 2, 'Iphone',10000,'Mouse',400,'Teclado',450,'Fone',250)
    print('-'*50)
    print(f'{"LISTAGEM DE PREÇOS": ^50}')
    print('-'*50)
    for i,produto in enumerate(produtos):
        if(i%2==0):
            print(f'{produto:.<35}R$',end='')
        else:
            print(f'{produto: >10.2f}')
    print('-'*50)
desafio76()