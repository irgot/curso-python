#!/home/igor/.virtualenv/curso/bin/python
import math
import random
import pygame
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

desafio21()



# desafio3()

