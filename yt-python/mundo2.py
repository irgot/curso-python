def desafio36():
    vc = float(input("Digite o valor da casa: R$"))
    sa = float(input('Digite o valor do seu salário: R$'))
    qa = float(input('Digite em quantos anos pretende pagar: '))

    vm = vc/(qa*12)
    tpsal = sa*0.3
    if vm>tpsal:
        print('Empréstimo negado, valor da prestação de R${:.2f} excede o 30% de seu salário: R${:.2f}'.format(vm,tpsal))
    else:
        print('Parabéns, empréstimo aprovado! prestação = R${:.2f}'.format(vm))


def desafio37():
    n1 = int(input('Digite um número qualquer: '))
    cv = str(input('''Converter: 
    1 - Binário
    2 - Octal
    3 - Hexadecimal
'''))
    acum=n1
    dig=[]
    
    base={'1':2,'2':8,'3':16}

    while acum>0:
        res=acum%base[cv]
        acum=acum//base[cv]
        if base[cv]==16 and res>=10:
            if res==10:
                res='A'
            elif res==11:
                res='B'
            elif res==12:
                res='C'
            elif res==13:
                res='D'
            elif res==14:
                res='E'
            elif res==15:
                res='F'
            pass
                    
        dig.append(res)
        pass
    
    i=len(dig)-1

    print('Base:{} = '.format(base[cv]),end='')
    while i>=0:
        print(dig[i],end='')
        i=i-1
    print(' ')
    print('bin: {} == oct: {} == hex: {}'.format(bin(n1),oct(n1),hex(n1)))
    
def desafio38():
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    if n1>n2:
        print('Primeiro valor é maior')
    elif n2>n1:
        print('Segundo valor é maior')
    else:
        print('Não existe valor maior, os 2 são iguais')
        pass
    pass


def desafio39():
    from datetime import date
    ano = date.today().year
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano - ano_nascimento
    if idade>18:
        print('Passou do tempo de alistamento. Está {} anos atrasado.'.format(idade-18))
    elif idade<18:
        print('Ainda vai se alistar. Ainda faltam {} anos para se alistar.'.format(18-idade))
    else:
        print('É a hora de se alistar.')
    

def desafio40():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = (n1+n2)/2
    if m<5:
        status='Reprovado'
    elif m<7:
        status='Recuperação'
    elif m>=7:
        status='Aprovado'
    print('Situação do aluno: {}'.format(status))


def desafio41():
    from datetime import date
    an = int(input('Digite o ano de nascimento: '))
    aa = date.today().year
    idade = aa-an
    if idade<=9:
        cat = 'MIRIM'
    elif idade<=14:
        cat = 'INFANTIL'
    elif idade<=19:
        cat = 'JUNIOR'
    elif idade<=20:
        cat = 'SENIOR'
    else:
        cat = 'MASTER'    
    print('Categoria: {}'.format(cat))

def desafio42():
    l1 = float(input('Digite a medida do 1º lado do triângulo: '))
    l2 = float(input('Digite a medida do 2º lado do triângulo: '))
    l3 = float(input('Digite a medida do 3º lado do triângulo: '))
    
    if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
        print('Os lados podem formar um triângulo.')
        if l1==l2 and l2==l3:
            cat = 'Equilátero'
        elif l1==l2 or l2==l3:
            cat = 'Isósceles'
        else:
            cat = 'Escaleno'
        print('Categoria: {}'.format(cat))
        pass
    else:
        print('Os lados não podem formar um triângulo.')
        pass

def desafio43():
    peso = float(input('Digite o peso da pessoa: '))
    altura = float(input('Digite a altura da pessoa: '))
    imc = peso/(altura**2)
    print('Seu imc é:{:.1f}'.format(imc))
    if imc<18.5:
        print('Você está abaixo do peso.')
    elif imc<25:
        print('Parabéns, você está no peso ideal.')
    elif imc<30:
        print('Você está com sobrepeso.')
    elif imc<40:
        print('Você está obeso.')
    else:
        print('Você se encaixa na categoria de obesidad mórbida.')

def desafio44():
    preco = float(input('Digite o preço do produto: R$'))
    print('''Escolha a condição de pagamento:
1) À vista: 10% de desconto,
2) À vista no cartão: 5% de desconto,
3) Em até 2x sem juros,
4) 3x ou mais 20%.''')
    condicao=int(input())
    if condicao==1:
        precon=preco*0.9
    elif condicao==2:
        precon=preco*0.95
    elif condicao==4:
        precon=preco*1.2
    else:
        precon=preco
    print('Total a pagar: R${}'.format(precon))
    

def desafio45():
    from random import randint
    jk = {'1':'Pedra','2':'Papel','3':'Tesoura'}
    escolha = int(input('''
1: Pedra, 
2: Papel, 
3: Tesoura
Digite sua escolha: '''))
    computador = randint(1,3)
    print('Você escolheu: {}'.format(jk[str(escolha)]))
    print('Computador escolheu: {}'.format(jk[str(computador)]))
    if escolha == computador:
        print('Empate')
    elif escolha==1:
        if computador==2:
            print('Perdeu!')
        else:
            print('Ganhou!')
    elif escolha==2:
        if computador==3:
            print('Perdeu!')
        else:
            print('Ganhou!')
    elif escolha==3:
        if computador==1:
            print('Perdeu!')
        else:
            print('Ganou!')
    


    

desafio37()
