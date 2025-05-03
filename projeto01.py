#Exercicio 1
# dada uma lista , devolver em string
def lista_para_string(lista):
    if len(lista) ==0:
        return ''
    elif len(lista) ==1:
        return lista[0]
    else:
        corpo = ', '.join(lista[:-1])
        return corpo + ' e ' + lista[-1]
#teste
testes = [
    [],
    ['gato'],
    ['gato', 'cachorro'],
    ['gato', 'cachorro', 'rato']
]

for t in testes:
    print(lista_para_string(t))
