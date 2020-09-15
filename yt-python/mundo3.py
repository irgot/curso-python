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



def desafio84():
    mais_pesadas=list()
    mais_leves=list()
    pessoas=list()
    pessoa=list()
    
    while True:
        c=' '
        pessoa.append(str(input('Digite o nome de uma pessoa: ').capitalize()))
        pessoa.append(float(input('Digite o peso desta pessoa: ')))
        pessoas.append(pessoa[:])
        pessoa.clear()
        while c not in 'SN':
            c=str(input('Deseja cadastrar outra pessoa? [S/N]')).upper().strip()[0]
        if c=='N':
            break
    for indx,pessoa in enumerate(pessoas):
        if indx==0:
            mais_pesadas.append(pessoa[:])
            mais_leves.append(pessoa[:])
        else:
            if pessoa[1]>mais_pesadas[0][1]:
                mais_pesadas.clear()
                mais_pesadas.append(pessoa[:])
            elif pessoa[1]==mais_pesadas[0][1]:
                mais_pesadas.append(pessoa[:])
                pass
            if pessoa[1]<mais_leves[0][1]:
                mais_leves.clear()
                mais_leves.append(pessoa[:])
            elif pessoa[1]==mais_leves[0][1]:
                mais_leves.append(pessoa[:])
                pass
            pass
        pass
    print('='*32)
    print(f'Foram cadastrada(s) {len(pessoas)} pessoa(s).')
    print(f'O maior peso foi: {mais_pesadas[0][1]} e as pessoas foram: ',end='')
    for pessoa in mais_pesadas:
        print(f'{pessoa[0]}, ',end='')
    print(' ')
    print(f'O menor peso foi: {mais_leves[0][1]} e as pessoas foram: ', end='')
    for pessoa in mais_leves:
        print(f'{pessoa[0]}, ',end='')
    print(' ')

    pass
def desafio85():
    numeros=list()
    pares=list()
    impares=list()
    for i in range(0,7):
        numero=int(input(f'Digite o {i+1}º número: '))
        if numero%2==0:
            pares.append(numero)
        else:
            impares.append(numero)
    numeros.append(sorted(pares[:]))
    numeros.append(sorted(impares[:]))
    print(f'Os números pares foram: {numeros[0]}')
    print(f'Os números impares foram: {numeros[1]}')
    pass
def desafio86():
    matriz=list()
    linha=list()
    for i in range(0,3):
        for j in range(0,3):
            numero=int(input(f'Digite um valor para [{i},{j}]: '))
            linha.append(numero)
            pass
        matriz.append(linha[:])
        linha.clear()
        pass
    for linha in matriz:
        for numero in linha:
            print(f'[{numero:.^5}]',end='')
            pass
        print(' ')
    print(matriz)
    


    pass
def desafio87():
    matriz=list()
    linha=list()
    somapares=soma3coluna=maiorsegundalinha=0
    for i in range(0,3):
        for j in range(0,3):
            numero=int(input(f'Digite um valor para [{i},{j}]: '))
            linha.append(numero)
            pass
        matriz.append(linha[:])
        linha.clear()
        pass
    print('='*32)
    for i,linha in enumerate(matriz):
        for j,numero in enumerate(linha):
            print(f'[{numero:.^5}]',end='')
            somapares+=numero if numero%2==0 else 0
            if j==2:
                soma3coluna+=numero
            if i==1:
                if numero>maiorsegundalinha:
                    maiorsegundalinha=numero
                    pass
                pass
            pass
        print(' ')
        pass
    
    print('='*32)
    print(f'A soma de todos os valores pares digitados: {somapares}')
    print(f'A soma dos valores da terceira coluna: {soma3coluna}')
    print(f'O maior valor da segunda linha é: {maiorsegundalinha}')            
    pass
def desafio88():
    from random import randint
    palpites=list()
    jogo=list()
    numero=jogos=i=0
    print('='*80)
    print(f'{"GERADOR DE JOGOS DA MEGASENA!":=^80}')
    print('='*80)
    jogos=int(input('Digite a quantidade de jogos de 6 números a serem geradas: '))
    for i in range(0,jogos):
        jogo.clear()
        for j in range(0,6):
            numero=0 
            while numero in jogo or numero==0:
                numero=randint(1,60)
                pass
            jogo.append(numero)
            pass
        palpites.append(jogo[:])
        pass
    for indx,jogo in enumerate(palpites):
        print(f'{indx+1:3}º Jogo: [ ',end='')
        jogo.sort()
        for jdx,numero in enumerate(jogo):
            if jdx<5:
                print(f'{numero:02}',end=', ')
            else:
                print(f'{numero:02}',end=' ')
        print('] ')
    print(f'{"< Boa Sorte! >":=^80}')
    pass
def desafio89():
    alunos=list()
    aluno=list()
    notas=list()
    nota=0
    nome=''    
    while True:
        c=' '
        nome=str(input('Digite o nome do aluno: '))
        for i in range(0,2):
            nota=float(input(f'Digite a nota {i+1}º do aluno: '))
            notas.append(nota)
        aluno.append(nome)
        aluno.append(notas[:])
        alunos.append(aluno[:])
        aluno.clear()
        notas.clear()
        while c not in "SN":
            c=str(input('Deseja cadastrar outro aluno? [S/N]')).upper().strip()[0]
        if c=='N':
            break
        pass
    print('='*60)
    print(f'{"BOLETIM":=^60}')
    print('='*60)
    print(f'{"No.":<5} {"Nome":<40} {"Media":>10}')
    print('-'*60)
    for indx,aluno in enumerate(alunos):
        somanota=0
        media=0
        print(f'{indx:<5}', end='')
        print(f'{aluno[0]:<40}', end='')
        for nota in aluno[1]:
            somanota+=nota
        media=somanota/len(aluno[1])
        print(f'{media:>10}')
        pass
    print('-'*60)
    while True:        
        print('='*60)
        id = int(input('Mostrar nota de qual aluno? (999 para sair)'))
        if id==999:
            break
        else:
            print(f'Nota de {alunos[id][0]} são {alunos[id][1]}')
    print('='*60)
    print('Volte sempre!')

desafio89()