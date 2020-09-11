#!/home/igor/.virtualenv/curso/bin/python
import math
import random
import requests

def desafio2():

    n1 = input('Digite um número:')
    n2 = input ('Digite outro número:')
    s = int(n1)+int(n2)
    print('A soma é:', s);
    print ('a soma vale: {}'.format(s))
    print('a soma entre {0} e {1} vale {2}'.format(n1, n2, s))

###
def desafio3():
    n3 = input('Digite algo: ')
    print('O tipo primitivo desse valor é: {}'.format(type(n3)))
    print('Tem somente espaços? {}'.format(n3.isspace()))
    print('É um número? {}'.format(n3.isnumeric()))
    print('É alfabético? {}'.format(n3.isalpha()))
    print('É alfanumérico? {}'.format(n3.isalnum()))
    print('Está em maiusculas? {}'.format(n3.isupper()))
    print('Está em minusculas?  {}'.format(n3.islower()))
    print('Está capitalizada? {}'.format(n3.istitle()))

def desafio16():
    n1 = float(input('Digite um número qualquer para saber sua porção inteira: '))
    truncado = math.trunc(n1)
    print('A porção inteira do número: {} é: {}'.format(n1,truncado))


def desafio17():
    cat1 = float(input('Cateto adjacente: '))
    cat2 = float(input('Cat oposto: '))
    hipo = math.hypot(cat1,cat2)
    print('Hipotenusa = {:.2f}'.format(hipo))
    # print('hipo2: {}'.format((cat1**2+cat2**2)**0.5))

def desafio18():
    ang = float(input('Digite o angulo: '))
    sen = math.sin(math.radians(ang))
    cos = math.cos(math.radians(ang))
    tang = math.tan(math.radians(ang))
    print('Seno: {:.2f} Cosseno: {:.2f} Tangente:{:.2f}'.format(sen,cos,tang))


def desafio19():
    lista=[]
    i=1
    while i<=4:
        lista.append((input('Digite o nome do {} aluno: '.format(i))))
        i=i+1
        pass    
    ganhador = random.randrange(1,4)
    print('O ganhador é: {}'.format(lista[ganhador]))

def desafio20():
    lista=[]
    # listaOrdem=[]
    i=1
    while i<=4:
        lista.append((input('Digite o nome do aluno {}: '.format(i))))                
        i=i+1
        pass

    random.shuffle(lista)
    # while len(listaOrdem)<4:
    #     r = random.randint(1,4)
    #     if r not in listaOrdem:
    #         listaOrdem.append(r)
    #     pass
    for idx,lo in enumerate(lista):        
        print('A ordem será: {}º : {}'.format(idx+1,lo))


def desafio21():
    pygame.init()
    pygame.mixer.music.load('i.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()



def aula09():
    frase = 'Curso em Vídeo Python'


def desafio22():
    nome = input('Digite seu nome completo: ')
    print('Nome em maiusculas: {}'.format(nome.upper()))
    print('Nome em minusculas: {}'.format(nome.lower()))
    print('Quantas letras ao todo (sem os espaços): {}'.format(len(nome.replace(' ',''))))
    print('Quantas letras tem o primeiro nome: {}'.format(len(nome.split()[0])))


def desafio23():
    numero = int(input('Digite um número de 0-9999: '))
    # if len(numero)>=1:
    #     print('Unidade: {}'.format(numero[-1]))
    # if len(numero)>=2:
    #     print('Dezena: {}'.format(numero[-2]))
    # if len(numero)>=3:
    #     print('Centena: {}'.format(numero[-3]))
    # if len(numero)>=4:
    #     print('Milhar: {}'.format(numero[-4]))
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10

    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena: {}'.format(c))
    print('Milhar: {}'.format(m))
    

def desafio24():
    cidade=input('Digite o nome de sua cidade: ').strip()
    if(cidade.upper().startswith('SANTO')):
        print('Sua cidade começa com Santo')
    else:
        print('Sua cidade não começa com Santo')

def desafio25():
    nome = input('Digite o seu nome: ').strip()
    if('SILVA' in nome.upper()):
        print('Seu nome tem Silva')
    else:
        print('Seu nome não tem Silva')

def desafio26():
    frase = input('Digite uma frase: ').strip()
    print('A letra ''A'' aparece {}x'.format(frase.upper().count('A')))
    print('A primeira posição que ela aparece é: {}'.format(frase.upper().find('A')))
    print('A ultima posição que ela aparece é: {}'.format(frase.upper().rfind('A')))

def desafio27():
    nome = input('Digite seu nome: ').strip()
    print('Primeiro nome: {}'.format(nome.split()[0]))
    print('Ultimo nome: {}'.format(nome.split()[-1]))

def desafio28():
    print('Pensando em um número entre 0 e 5...')
    n1 = random.randint(0,5)
    n2 = int(input('Tente adivinhar: '))
    if n1==n2:
        print('Parabéns, você acertou!')
    else:
        print('Que pena, você errou!')
    print('Parabéns!' if n1==n2 else "Que Pena! o número era: {}".format(n1))

def desafio29():
    v1=float(input('Digite a velocidade do veículo:'))
    if v1>80:
        print('Multado! R${:.2f}'.format((v1-80)*7))
    
def desafio30():
    n1=int(input('Digite um número para saber se é par ou impar: '))
    if (n1%2)==0:
        print("O número é par")
    else:
        print('O numero é impar')


def desafio31():
    d1 = float(input('Digite a distância da viagem: '))
    if d1<=200:
        valor=d1*0.5
    else:
        valor=d1*0.45
    print('O valor da viagem é de: R${:.2f}'.format(valor))

def desafio32():#anobissexto
    a1 = int(input('Digite o ano para saber se é bissexto: '))
    print("É bissexto." if a1%4==0 and not(a1%100==0 and a1%400!=0) else "Não é bissexto.")


def desafio33():#comparar 3 numeros
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    n3 = int(input('Digite o 3º número: '))

    if n1>n2: 
        if n1>n3:
            print('1º é o maior número')
            print('2º é o menor número' if n2<n3 else '3º é o menor número')
        else:
            print('3º é o maior número')
            print('2º é o menor número')
    else:
        if n2>n3:
            print('2º é o maior número')
            print('3º é o menor número' if n3<n1 else '1º é o menor número')
        else:
            print('3º é o maior número')
            print('1º é o  menor número')
    
    menor = n1
    if n2<n3 and n2<n1:
        menor=n2
    if n3<n2 and n3<n1:
        menor=n3

    maior=n1
    if n2>n3 and n2>n1:
        maior=n2
    if n3>n2 and n3>n1:
        maior=n3
    
    print('Maior:{}, menor:{}'.format(maior,menor))


    

def desafio34():#salario
    s1 = float(input("Digite o salário do funcionário: R$"))
    if s1>1250:
        sn=s1*1.1
    else:
        sn=s1*1.15
    
    print("Novo salario: R${:.2f}".format(sn))

def desafio35():#comprimento retas
    l1=float(input('Digite o comprimento do 1º lado: '))
    l2=float(input('Digite o comprimento do 2º lado: '))
    l3=float(input('Digite o comprimento do 3º lado: '))
    message=('Esse triângulo não pode existir!')
    if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
        message='Esse triângulo pode existir!'
    
    print(message)




def aulacores():
    print('\033[0;30;41m Teste\033[m')
    print('\033[4;33;44m Teste\033[m')
    print('\033[1;35;43m Teste\033[m')
    print('\033[30;42m Teste\033[m')
    print('\033[m Teste\033[m')
    print('\033[7;30m Teste\033[m')
    


aulacores()