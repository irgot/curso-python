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
    maior = 0
    menor = 0
    numeros=(randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60))
    print(f'Os números gerados foram:{numeros}')
    for i,n in enumerate(numeros):        
        if i==0:
            menor=n
            maior=n
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    print(f'O menor número sorteado foi: {max(numeros)} e o maior foi {min(numeros)}.')

def desafio75():
   
    numeros=(int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),int(input('Digite o 3º número: ')),int(input('Digite o 4º número: ')))
    print(f'O número 9 apareceu: {numeros.count(9)} vezes.')
    try:
        posicao = numeros.index(3)
        print(f'O número 3 apareceu na {posicao+1}ª posição.')
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
            print(f'{produto:.<35}',end='')
        else:
            print(f'R${produto: >10.2f}')
    print('-'*50)


def desafio77():
    palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')    
    for palavra in palavras:
        print (f'Na palavra {palavra.upper()} temos: ', end='')
        for letra in palavra:
            if letra.upper() in 'AEIOU':
                print (f'{letra.lower()} ',end='')
                pass
            pass
        print(' ')
        pass
    pass

def desafio78():
    valores = []
    for i in range(0,5):
        valores.append(int(input(f'Digite o valor {i}: ')))
    print('-='*32)
    print(f'Você digitou os valores: {valores}')
    print(f'O maior valor digitado foi: {max(valores)} nas posições: ', end='')
    
    for index,valor in enumerate(valores):
        if valor==max(valores):
            print(index,end='... ')
            pass
        pass    
    del(index)
    del(valor)
    print(' ')
    print(f'O menor valor digitado foi: {min(valores)} nas posições: ', end='')
    for index,valor in enumerate(valores):
        if valor==min(valores):
            print(index,end='... ')
            pass

        pass
    print(' ')
    


def desafio79():
    c=' '
    numeros=[]
    while(c!='N'):
        c=' '
        n = int(input('Digite um número: '))
        if n in numeros:
            print('Valor duplicado!')
        else:
            numeros.append(n)
        while(c not in 'SN'):
            c=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    numeros.sort()
    print(f'Você digitou os valores: {numeros}')
    

def desafio80():
    lista=list()
    for i in range(0,5):
        n = int(input('Digite um valor: '))
        if i==0:
            print(f'Foi adicionado no final da lista...')
            lista.append(n)
        else:
            for index,l in enumerate(lista):
                if n<=l :
                    lista.insert(index,n)
                    print(f'Foi adicionado na posição: {index} da lista...')
                    break                    
                if index==len(lista)-1:
                    lista.append(n)
                    print(f'Foi adicionado no final da lista...')
                    break
                pass            
            pass
        
    print(f'Os valores digitados em ordem foram: {lista}')
            
def desafio81():
    lista=[]
    c=' '
    while c!='N':
        c=' '
        lista.append(int(input('Digite um número: ')))
        while c not in 'SN':
            c=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print(f'Foram digitados {len(lista)} números.')
    lista.sort(reverse = True)
    print(f'A lista de valores em ordem decrescente: {lista}')
    if 5 in lista:
        print(f'O valor 5 está na lista.')
    else:
        print(f'O valor 5 não foi encontrado na lista')

def desafio82():
    lista = []
    lpar = []
    limpar = []
    c=' '
    while c!='N':
        c=' '
        lista.append(int(input('Digite um valor: ')))
        while c not in 'SN':
            c=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    for l in lista:
        if l%2==0:
            lpar.append(l)
        else:
            limpar.append(l)
        pass
    print(f'A lista digitada foi: {lista}')
    print(f'A lista de números pares gerada foi: {lpar}')
    print(f'A lista de números impares gerada foi: {limpar}')


def desafio83():
    cl = 0
    cr = 0
    erro = False
    expressao = str(input('Digite uma expressão: '))
    for l in expressao:
        if l=='(':
            cl+=1
        if l==')':
           cr+=1           
        if cr>cl :
            erro=True
    if cr!=cl:
        erro=True
    print('Sua expressão está errada!' if erro else 'Sua expressão está correta!')    
    pass

desafio83()