# pip install numpy
# conda install numpy
import numpy as np

"""
Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais.

O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ).

Divida final=compra – desconto, valor do desconto se compra for
        entre 100 e 200 é 5%,
        entre  200 e 500 é 10%
        se superior a 500 é 15%.


O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 5v.

O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v).

"""
lista = []


def calcDiv(valor):
    if valor < 100:
        return valor

    if np.arange(100, 200, 0.01).__contains__(valor):
        return valor * 0.95

    if valor in np.arange(200, 500, 0.01):
        return valor * 0.9

    return valor * 0.85



def find_cliente(id_cli: int):
    if id_cli == 0 or id_cli > lista.__len__():
        return None

    return lista[id_cli - 1]


def val_compra(val: int):
    if val < 0:
        return (False, None)
    return (True, val)


# input
nome_cli = "Joao"
morada = "Lisboa"
tel = 1234
nif = 1234
compra = 50

# gerar num Cli

num_cli = lista.__len__() + 1

# calc Divfin

div_fin = calcDiv(compra)

compraCliente = [num_cli, nome_cli, morada, tel, nif, compra, div_fin]
lista.append(compraCliente)

"""
# input
nome_cli = "Joao"
morada = "Lisboa"
tel = 1234
nif = 1234
compra = 100

# gerar num Cli

num_cli = lista.__len__() + 1

# calc Divfin

div_fin = calcDiv(compra)

compraCliente = [num_cli,nome_cli,  morada, tel, nif, compra, div_fin]
lista.append(compraCliente)



# input
nome_cli = "Joao"
morada = "Lisboa"
tel = 1234
nif = 1234
compra = 200

# gerar num Cli

num_cli = lista.__len__() + 1

# calc Divfin

div_fin = calcDiv(compra)

compraCliente = [num_cli,nome_cli,  morada, tel, nif, compra, div_fin]
lista.append(compraCliente)



# input
NomCli = "Joao"
morada = "Lisboa"
tel = 1234
nif = 1234
compra = 500

# gerar num Cli

num_cli = lista.__len__() + 1

# calc Divfin

div_fin = calcDiv(compra)

compraCliente = [num_cli,nome_cli,  morada, tel, nif, compra, div_fin]
lista.append(compraCliente)


for elm in lista:
    print(elm)


print("----------")

print(find_cliente(2))

print(find_cliente(0))
print(find_cliente(6))

"""



print(
    list(range(0,10))
)
print(
   np.arange(0,10, dtype='float')
)


lst = [1,2,True, "Nome"]
print(lst[0])
print(lst[2])
print(lst[3])

print(np.array(lst))

mat = [[0,1,2],
       [3,4,5],
       [6,7,8]]


np_mat = np.array(mat)


print(np_mat[2][2])
print(np_mat[2,2])

