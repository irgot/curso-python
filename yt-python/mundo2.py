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



def desafio46():
    from time import sleep
    print('Contagem regressiva:')
    sleep(1)
    for i in range(10,0,-1):
        sleep(1)
        print(i)
    print('BOOOMMMMMM PUM PAAAAA')
    

def desafio47():
    for i in range(2,51,2):
        print(i)



def desafio48():
    soma=0
    for i in range(1,501,2):
        if i%3==0:
            soma=soma+i
        pass
    print(soma)
    pass

def desafio49():
    n1 = int(input('Digite um número para imprimir sua tabuada: '))
    for i in range(1,11):
        print('{} * {:2} = {:2}'.format(n1,i,n1*i))


def desafio50():
    soma=0
    for i in range(0,6):
        n = int(input('Digite um número: '))
        if n%2==0:
            soma=soma+n
            pass
        pass
    print(soma)



def desafio51():
    pt = int(input('Digite o primeiro termo: '))
    ra = int(input('Digite a razão aritimética: '))
    pa=pt
    for i in range(0,10):
        print(pa,end=', ')
        pa=pa+ra
        pass
    print('\n')

def desafio52():
    n1 = int(input('Digite um número: '))
    primo=True
    divisivel=0
    for i in range(1,n1+1):
        if n1%i==0 and n1!=i and i!=1 and divisivel==0:
            primo=False
            divisivel=i
            pass
        pass
    if n1==1:
        primo=False
    if primo:
        print('Número {} é primo'.format(n1))
    else:
        print('Número {} não é primo. Pois é divisível por {}.'.format(n1,divisivel))


def desafio53():
    f1 = str(input('Digite uma frase:')).replace(' ','')
    f2 = f1[::-1]

    # jeito porco
    # for i in range(len(f1),0,-1):
    #     f2=f2+f1[i-1]
    
    print(f1,f2)
    if f1.upper()==f2.upper():
        print('A frase é um palíndromo')
    else:
        print('A frase não é um palíndromo')

def desafio54():
    from datetime import date
    cmaior=0
    cmenor=0
    ano_atual = date.today().year
    for i in range(1,8):
        ano = int(input('Digite o ano de nascimento: '))
        idade=ano_atual-ano
        if idade>=21:
            cmaior=cmaior+1
        else:
            cmenor=cmenor+1
            
    print('{} pessoas são de maior idade e {} são de menor.'.format(cmaior,cmenor))

def desafio55():
    pmaior=0
    pmenor=0
    for i in range(1,6):
        peso=float(input('Digite o peso da pessoa: '))
        if i==1:
            pmaior=peso
            pmenor=peso        
        else:
            if peso>pmaior:
                pmaior=peso
            if peso<pmenor:
                pmenor=peso
            pass
    print('{} foi o maior peso lido, e {} foi o menor.'.format(pmaior,pmenor))

def desafio56():
    cmulheres20=0
    media=0
    somaidade=0
    c_idade=0
    maisvelho=''
    idademv = 0
    for i in range(1,5):
        nome=str(input('Digite o nome da pessoa: '))
        idade = int(input('Digite a idade da pessoa: '))
        sexo = str(input('Digite [M] para masculino ou [F] para feminino: '))
        somaidade=somaidade+idade
        c_idade=c_idade+1
        if idademv<idade and sexo.upper()=='M':
            idademv=idade
            maisvelho=nome
            pass
        if sexo.upper()=='F' and idade<20:
            cmulheres20=cmulheres20+1
            pass
        pass
    print('{} é a média de idade.'.format(somaidade/c_idade))
    print('{} é o homem mais velho com {} anos'.format(maisvelho,idademv))
    print('{} mulheres tem menos de 20 anos.'.format(cmulheres20))



def desafio57():
    s='A'
    while(s not in 'MF'):
        s=str(input('Digite seu sexo [M/F]: ')).upper()
    print('Masculino' if s=='M' else 'Feminino')

def desafio58():
    from random import randint
    numero_pc = randint(1,10)
    numero_escolhido=0
    tentativas=0
    while(numero_pc!=numero_escolhido):
        numero_escolhido = int(input('Digite o número que o computador pensou de 1 a 10: '))
        tentativas+=1
        if(numero_escolhido!=numero_pc):
            print('Errou! Tente novamente!')            
    print('Acertou mizeravi! Em {} tentativas.'.format(tentativas))


def desafio59():
    m=4
    while(m!=5):
        if m==4:
            n1 = float(input('Digite o 1º número: '))
            n2 = float(input('Digite o 2º número:'))
        
        if m==1:
            print('A soma dos 2 números é: {}'.format(n1+n2))
        if m==2:
            print('A multiplicação dos números é:{}'.format(n1*n2))
        if m==3:
            if n1>n2:
                print('O 1º número:{}  é maior que o 2º número:{}'.format(n1,n2))
            elif n2>n1:
                print('O 2º número:{}  é maior que o 1º número:{}'.format(n2,n1))
            else:
                print('O 1º número: {} e o 2º número: {} são iguais.'.format(n1,n2))
        print('''
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos números
[5] - sair do programa''')
        m=int(input('Escolha uma opção: '))



def desafio60():
    n1 = int(input('Digite um número para saber seu fatorial:'))
    acum=1
    fat=n1    
    # while(fat>0):
    #     acum*=fat
    #     # print(' * {}'.format(fat) if fat!=n1 else '{}'.format(fat) ,end='')
    #     fat-=1
    # fat=n1
    # acum=1
    for i in range(fat,0,-1):
        acum*=i
        print(' * {}'.format(i) if i!=n1 else '{}'.format(i) ,end='')
        
    print(' = {}'.format(acum))


def desafio61():
    pt = int(input('Digite o primeiro termo de uma progressão aritmética: '))
    ra = int(input('Digite a razão: '))
    pa = pt
    # print('{}'.format(pa),end='')
    qt=0
    t=10
    while(t!=0):
        qt+=t
        while pa<pt+(ra*qt):
            if (pa+ra<pt+(ra*qt)):
                print('{} - '.format(pa),end='')
            else:
                print('{}'.format(pa),end='')
            pa+=ra
            pass            
        print('')            
        t=int(input('Quer imprimir mais quantos termos?'))


def desafio63():
    n1 = int(input('Digite a quantidade da sequência de fribonacci: '))
    c = 0
    atu = 0
    ant1 = 0
    ant2 = 0
    while c<n1:        
        c+=1
        print('{} -> '.format(atu),end='')        
        if(atu==0):
            ant=0
            atu=1
        else:
            ant2=ant1
            ant1=atu
            atu=ant1+ant2            
            
def desafio64():
    n=0
    acum=0
    count=0
    while(n!=999):        
        n=int(input('Digite um número: '))
        if(n!=999):
            acum+=n
            count+=1
            pass
        pass
    print('Acumulado: {} e Quantidade: {}'.format(acum,count))


def desafio65():
    n = acum = count = menor = maior = 0
    continua=True
    while(continua):        
        n=int(input('Digite um número: ').strip())
        if(count==0):
            maior=n
            menor=n
        else:
            maior=n if n>maior else maior
            menor=n if n<menor else menor
        acum+=n
        count+=1
        continua=input('Deseja continuar [S/N]?').upper().strip()[0]=='S'        
        pass
    print('A média é: {}'.format(acum/count))
    print('O maior valor digitado foi: {}'.format(maior))
    print('O menor valor digitado foi: {}'.format(menor))

def desafio66():
    count = acum = 0
    while True:
        n1 = int(input('Digite um número ou [999] para sair: '))
        if n1 == 999:
            break
        count+=1
        acum+=n1
    print(f'Foram digitados {count} números e a soma deles é {acum}')

    pass
def desafio67():
    while True:
        n1 = int(input('Digite um número para saber sua tabuada ou um número negativo para sair:'))
        if(n1<0):
            break
        print('#'*32)
        for i in range(1,11):            
            print(f'{n1:2} * {i:2} = {n1*i:3}')
        print('#'*32)

def desafio68():
    from random import randint
    countv=0    
    while True:
        poi=''
        poie=''
        n=randint(1,20)
        while poi not in ('P','I'):
            poi = str(input('Escolha par ou ímpar [P/I]')).strip().upper()[0]
        poie = 'Par' if n%2==0 else 'Impar'
        print('#'*32)
        print('Você escolheu par.' if poi == 'P' else 'Você escolheu impar.')
        print(f'O número selecionado foi {n} que é {poie}.')
        
        r=n%2
        if poi=='P' and r == 1 :
            print(f'{"Perdeu":-^32}')
            print('#'*32)
            break
        if poi=='I' and r == 0 :
            print(f'{"Perdeu":-^32}')
            print('#'*32)
            break
        print(f'{"Ganhou":-^32}')
        print('#'*32)
        countv+=1
    print(f'Você conseguiu um total de {countv} vitórias.')

def desafio69():
    countmais18 = counth = countmulhermenos20 = 0    
    
    while True:
        continuar=' '    
        sexo=idade=' '
        idade = int(input('Digite a idade da pessoa: '))
        while sexo not in 'MF':
            sexo=input('Digite o sexo [M/F]').strip().upper()[0]
        if idade>18:
            countmais18+=1
        if sexo=='M':
            counth+=1
        if idade<20 and sexo=='F':
            countmulhermenos20+=1
        while continuar not in 'SN':
            continuar=input('Deseja continuar? [S/N]').strip().upper()[0]
        if continuar=='N':
            break
    
    print(f'{"Acabou o programa":-^50}')
    print(f'Existem {countmais18} pessoas maiores de 18 anos.')
    print(f'Foram cadastrados {counth} homens.')
    print(f'Foram cadastradas {countmulhermenos20} mulheres com menos de 20 anos.')


def desafio70():
    total_gasto = count_prod_mais_1000 = 0
    produto_mais_barato=' '
    preco_produto_mais_barato=-1
    while True:
        continuar=' '
        nome_produto = input('Digite o nome do produto: ')
        preco_produto = float(input('Digite o preço do produto: R$'))
        if total_gasto==0:
            preco_produto_mais_barato=preco_produto
            produto_mais_barato=nome_produto
        
        total_gasto+=preco_produto
        if preco_produto<preco_produto_mais_barato:
            preco_produto_mais_barato=preco_produto
            produto_mais_barato=nome_produto
        if preco_produto>1000:
            count_prod_mais_1000+=1
        while continuar not in 'SN':
            continuar=input('Deseja continuar [S/N] ? ').strip().upper()[0]
        if continuar=='N':
            break
        pass
    print(f'{"Fim da compra":=^32}')
    print(f'Total={total_gasto}')
    print(f'Total de {count_prod_mais_1000} produtos custam mais de R$1000,00')
    print(f'Produto mais barato:{produto_mais_barato} custando R${preco_produto_mais_barato:.2f} ')
        
def desafio71():
    qtd50 = qtd20 = qtd10 = qtd1 = 0
    valor_saque = int(input('Digite o valor inteiro a ser sacado: R$'))
    valor=valor_saque
    while valor>0:
        qtd50 = valor//50
        valor-=qtd50*50
        qtd20 = valor//20
        valor-=qtd20*20
        qtd10 = valor//10
        valor -= qtd10*10
        qtd1 = valor//1
        valor-=qtd1*1

    print(f'{qtd50:3} cedulas de R$50,00')
    print(f'{qtd20:3} cedulas de R$20,00')
    print(f'{qtd10:3} cedulas de R$10,00')
    print(f'{qtd1:3}  cedulas de R$01,00')



desafio71()
