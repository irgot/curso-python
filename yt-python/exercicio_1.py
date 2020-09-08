

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


# desafio3()

