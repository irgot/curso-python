def isFloat(n):
    f = n.replace('.','',1).isdigit()
    return f

def leiaDinheiro(msg):
    d=' '
    while True:
        d=input(msg)
        if ',' in d:
            d=d.replace(',','.')
        if isFloat(d):
            break
        else:
            print('Erro! Valor inválido.')    
    return(float(d))
    pass