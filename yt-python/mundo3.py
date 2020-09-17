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

def desafio90():
    aluno={}
    aluno['nome']=str(input('Nome: '))
    aluno['media']=float(input(f'Média do {aluno["nome"]}: '))
    if aluno['media']>=7:
        aluno['situacao']='Aprovado'
    elif aluno['media']>=5:
        aluno['situacao']='Recuperacao'
    else:
        aluno['situacao']='Reprovado'

    print(f'Nome é igual a {aluno["nome"]}')
    print(f'Média é igual a {aluno["media"]}')
    print(f'Situação é igual a {aluno["situacao"]}')
    pass
def desafio91():
    from random import randint
    from time import sleep
    from operator import itemgetter
    jogadores={}
    sorted2={}
    print('Valores sorteados:')
    for i in range(1,5):
        jogadores[f'jogador{i}']=randint(1,6)
        print(f'    O jogador{i} tirou: {jogadores[f"jogador{i}"]}')
        sleep(0.5)
    
    print('Ranking dos jogadores: ')
    sorted_jogadores = sorted(jogadores.items(),key=lambda x: x[1],reverse=True)    
    for  indx,jogador in enumerate(sorted_jogadores):
        print(f'    {indx+1}º lugar: {jogador[0]} com {jogador[1]}.')
        sleep(0.5)
    print('='*32)
    sorted2=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
    print(sorted2)


def desafio92():
    from datetime import date
    pessoa={}
    pessoa['nome']=str(input('Nome: ')).capitalize()
    pessoa['idade']=date.today().year-int(input('Ano de nascimento: '))
    pessoa['cpts']=int(input('CPTS (0 não tem): '))
    if pessoa['cpts']!=0:        
        pessoa['contratacao']=int(input('Ano de contratação: '))
        pessoa['salario']=float(input('Salário: '))
        pessoa['aposentadoria']=(35-(date.today().year-pessoa['contratacao']))+pessoa['idade']    
    print('=-'*32)
    print(pessoa)
    for indx,valor in pessoa.items():
        print(f'{indx} tem o valor {valor}.')



def desafio93():
    jogador={}
    jogador['nome']=input('Nome do jogador: ')
    partidas=int(input('Quantidade de partidas: '))
    jogador['gols']=[]
    jogador['total']=0
    for i in range(0,partidas):
        jogador['gols'].append(int(input(f'Gols na {i+1}ª partida: ')))
        # jogador['total']+=jogador['gols'][i]
    jogador['total']=sum(jogador['gols'])
    print('-='*32)
    print(jogador)
    print('-='*32)
    for chave,valor in jogador.items():
        print(f'O campo {chave} tem o valor {valor}.')       
    print('-='*32) 
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for indx,gols in enumerate(jogador['gols']):
        print(f'    =>Na partida {indx+1}, fez {gols} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')



def desafio94():
    pessoas=[]
    pessoa={}
    media=0
    somaIdade=0
    count_pessoa=0
    while True:        
        continuar= ' '
        count_pessoa+=1
        pessoa['nome']=input(f'Nome {count_pessoa}ª pessoa: ').capitalize()
        pessoa['sexo']=' '
        while pessoa['sexo'] not in 'MF':
            pessoa['sexo']=input('Sexo [M/F]: ').upper().strip()[0]
        pessoa['idade']=int(input('Idade: '))
        somaIdade+=pessoa['idade']
        while continuar not in 'SN':
            continuar=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        pessoas.append(pessoa.copy())
        pessoa.clear()
        if continuar in 'N':
            break
        pass
    print('-='*32)
    print(f'- O grupo tem {len(pessoas)} pessoas.')
    media=somaIdade/len(pessoas)
    print(f'- A media de idade é de {media} anos.')
    print(f'- As mulheres cadastradas foram: ',end='')
    for pessoa in pessoas:
        if pessoa['sexo']=='F':
            print(f'{pessoa["nome"]} ',end='')
    print('')    
    print(f'- Lista das pessoas que estão acima da média:')
    for pessoa in pessoas:
        if pessoa['idade']>media:
            for key,value in pessoa.items():
                print(f'{key} = {value}; ', end='')
            print('')
    print('<< ENCERRADO >>')

    pass

def desafio95():
    jogadores=[]
    jogador={}
    while True:
        c=' '
        jogador['nome']=input('Nome do jogador: ').capitalize().strip()
        partidas=int(input('Partidas: '))
        jogador['gols']=[]
        jogador['total']=0
        for i in range(0,partidas):
            jogador['gols'].append(int(input(f'Número de gols na {i+1}ª partida: ')))
            jogador['total']=jogador['gols'][i] if i==0 else jogador['total']+jogador['gols'][i]
        jogadores.append(jogador.copy())
        jogador.clear()
        while c not in 'NS':
            c = str(input('Deseja continuar? [S/N]')).upper().strip()[0]        
        if c=='N':
            break

        pass
    print('=-'*32)
    print(f'{"cod":<4}{"nome":<20}{"gols":<15}{"total":<5}')
    print('-'*45)
    # print(jogadores)
    for indx,jogador in enumerate(jogadores):
        print(f'{indx:<4}{jogador["nome"]:<20}{str(jogador["gols"]):<15}{jogador["total"]:<5}')
    print('-'*45)
    while True:
        indx=int(input('Mostrar dados de qual jogador? '))
        if indx==999:
            break
        if indx<len(jogadores):
            print(f'-- LEVANTAMENTO DO JOGADOR: {jogadores[indx]["nome"]}')
            for key,value in enumerate(jogadores[indx]["gols"]):
                print(f'    No jogo {key+1} fez {value} gols.')
                pass
            pass
        else:
            print(f'ERRO! Não existe jogador com o código {indx}! Tente novamente.')
            pass
        pass
    pass

def titulo(msg):
    print('-'*32)
    print(f'{msg:^32}')
    print('-'*32)
def desafio96():
    def area(l,c):
        print(f'A area do terreno é: {l*c}m²')    
    titulo('Controle de terrenos')
    largura=float(input('Largura do terreno (m): '))
    comprimento=float(input('Comprimento do terreno (m): '))
    area(largura,comprimento)

def desafio97():
    def escreva(txt):
        print(f'~'*(len(txt)+6))
        print(f'   {txt}   ')
        print(f'~'*(len(txt)+6))
    escreva('Gustavo Guanabara')
    escreva('Curso de Python no YouTube')
    escreva('CeV')

def desafio98():
    from time import sleep
    def contador(i,f,p):        
        if p==0:
            p=1
        if i<f:
            fim=f+1
            if p>0:
                passo=p
            else:
                passo=-p
        else:
            fim=f-1
            if p>0:
                passo=-p
            else:
                passo=p
        print('-='*32)    
        print(f'Contagem de {i} até {f} de {passo} em {passo}')
        for count in range(i,fim,passo):
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
        print('Fim!')
        print('-='*32)    
    
    contador(1,10,1)    
    contador(10,0,2)
    print('Agora é sua vez: ')
    i=int(input('Início: '))
    f=int(input('Fim: '))
    p=int(input('Passo: '))
    contador(i,f,p)

def desafio99():
    def maior(*num):
        from time import sleep
        # print(f'O maior valor é: {max(num)}')
        maior=0
        print('-='*32)
        print('Analisando os valores passados...')
        for i,v in enumerate(num):
            print(v,end=' ',flush=True)
            sleep(0.5)
            if i==0:
                maior=v
            elif v>maior:
                maior=v
                pass
            pass
        print(f'\nforam passados {len(num)} valores.')
        print(f'O maior valor é: {maior}')            
        pass
    maior(0,10,20,3,33,59,1,2,20)
    maior(4,7,0)
    maior(6)
    maior()

def desafio100():
    def sorteio(lst):
        from random import randint
        for i in range(0,5):
            lst.append(randint(0,99))
        pass
    def somaPar(lst):
        soma=0
        for v in lst:
            if v%2==0:
                soma+=v
                pass
            pass
        print(f'A soma dos valores pares é: {soma}')
        pass
        
    lista=[]
    sorteio(lista)
    print(lista)
    somaPar(lista)
    sorteio(lista)
    print(lista)
    somaPar(lista)
    pass

def desafio101():
    from datetime import date
    def voto(nascimento):
        idade=date.today().year - nascimento
        msg=f'Com {idade} anos: '
        if idade <16:
            msg+='NÃO VOTA.'
        elif idade <18:
            msg+='VOTO OPCIONAL.'
        elif idade<66:
            msg+='VOTO OBRIGATÓRIO.'
        else:
            msg+='VOTO OPCIONAL.'
        return msg
            
    
    titulo('Voto!')
    nascimento=int(input('Em que ano você nasceu: '))
    print(voto(nascimento))

def desafio102():    
    titulo('Func Fatorial')
    def fatorial(n,show=False):
        """Função para retornar o fatorial de um número.

        Args:
            n (int): Número a ser calculado o fatorial.
            show (bool, optional): Exibir ou não a conta. Defaults to False.

        Returns:
            str: String com o valor do fatorial ou o calculo em sí.
        """
        msg=''
        fatorial = 1
        for i in range(n,0,-1):
            if show:                
                msg+=f'{i} * ' if i>1 else f'{i} = '
                
            fatorial*=i
            

        msg+=f'{fatorial}'
        return msg    
    print(fatorial(5))
    print(fatorial(5,True))

def desafio103():
    titulo('Ficha jogador')
    def ficha(jogador='<desconhecido>',gols='0'):
        """Ficha do jogador

        Args:
            jogador (str, optional): Nome do Jogador. Defaults to '<desconhecido>'.
            gols (int, optional): Número de gols marcados. Defaults to 0.
        """
        jogador=jogador if jogador!='' else '<desconhecido>'
        gols=gols if gols!='' else '0'
        return(f'O jogador {jogador} fez {gols} gols no campeonato.')
    
    jogador=input('Nome do jogador: ')
    gols=input('Número de gols marcados: ')
    
    print(ficha(jogador,gols))
    
def desafio104():
    titulo('leia número inteiro')
    def leiaInt(str):
        n=' '        
        while not n.isnumeric():
            n=input(str)
            if not n.isnumeric():
                print('Erro! Digite um número inteiro')
                pass
            pass
        return int(n)
    n=leiaInt('Número: ')
    print(f'Você digitou o número {n}')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def desafio105():
    titulo('notas')
    def notas(*nota,sit=False):
        """Função para verificar notas* e retornar a situação de vários alunos

        Args:
            sit (bool, optional): retorna a situação da sala. Defaults to False.

        Returns:
            dict: retorna um dicionário com os valores
        """
        retorno={}        
        retorno['total']=len(nota)
        retorno['maior']=max(nota)
        retorno['menor']=min(nota)
        retorno['media']=sum(nota)/len(nota)
        if sit:
            if retorno['media']>=7:
                retorno['situacao']='BOA'
            elif retorno['media']>=5:
                retorno['situacao']='RAZOÁVEL'
            elif retorno['media']<5:
                retorno['situacao']='RUIM'
        return retorno
        pass
    resp=notas(3.5,2,6.5,2,7,4)
    print(resp)

def desafio106():
    def ajuda(com):
        help(com)
    from time import sleep
    titulo(bcolors.HEADER+'     Interactive help 2.0'+bcolors.ENDC)    
    while True:
        cmd = str(input(bcolors.OKBLUE+bcolors.BOLD+'HELP>'+bcolors.ENDC)).strip()
        if cmd=='fim':
            break
        print(f'{bcolors.BOLD}{bcolors.OKGREEN} Acessando o manual do comando {cmd} {bcolors.ENDC}')
        sleep(1)
        print(f'{bcolors.WARNING}',end='')
        ajuda(cmd)
        print(f'{bcolors.ENDC}')
        
    print(f'{bcolors.FAIL} Volte sempre! {bcolors.ENDC}')


def desafio107():
    import moeda
    p = float(input('Preço: R$'))
    print(f'A metade de {p} é {moeda.metade(p)}')
    print(f'O dobro de {p} é {moeda.dobro(p)}')
    print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
    print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')
def desafio108():
    import moeda
    p = float(input('Preço: R$'))
    print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
    print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
    print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')
def desafio109():
    import moeda
    p = float(input('Preço: R$'))
    m=True
    print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,m)}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,m)}')
    print(f'Aumentando 10%, temos {moeda.aumentar(p,10,m)}')
    print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,m)}')
def desafio110():
    import moeda
    p = float(input('Preço: R$'))
    moeda.resumo(p,80,35)
desafio110()





