def aumentar(p,a,m=False):
    r = p*(a/100)+p
    return moeda(r) if m else r
    pass
def diminuir(p,d,m=False):
    r = p-p*(d/100)
    return moeda(r) if m else r
    pass
def dobro(p, m=False):
    r = p*2
    return moeda(r) if m else r
    pass
def metade(p, m=False):
    r = p/2
    return moeda(r) if m else r
    pass

def moeda(v):
    f=f'R${v:2.2f}'
    f.replace('.',',')
    return(f)

def titulo(msg):
    print('-'*32)
    print(f'{msg:^32}')
    print('-'*32)

def resumo(p,a,d):
    titulo('RESUMO DO VALOR')
    m=True
    print(f'{"Preço analisado:":<20}{moeda(p):<7}')
    print(f'{"Dobro do preço:":<20}{dobro(p,m):<7}')
    print(f'{"Metade do preço:":<20}{metade(p,m):<7}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(p,a,m):<7}')
    print(f'{f"{d}% de redução:":<20}{diminuir(p,d,m):<7}')
    print('-'*32)