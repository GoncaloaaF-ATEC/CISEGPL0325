"""

Crie um programa que gere um cadastro de até 100 alunos, armazenando os seus nomes e turmas em duas listas separadas.

Requisitos do programa:

O programa deve apresentar um menu com as seguintes opções:

1 - Registar novo aluno

2 - Pesquisar alunos por nome ou turma

3 - Eliminar aluno por posição

4 - Sair do programa

Na opção Registar novo aluno, o utilizador deve poder adicionar o nome do aluno e a turma, respeitando o limite máximo de 100 registos.

Validações necessárias:

O nome do aluno não pode estar vazio nem conter apenas espaços.

A turma deve ser um valor válido (exemplo: “1.ºA”, “2.ºB”, “3.ºC”; pode definir quais turmas são válidas).

Não deve permitir registo duplicado do mesmo aluno na mesma turma.

Na opção Pesquisar alunos, o programa deve receber um termo de pesquisa e apresentar todas as entradas que contenham o nome ou a turma indicada, mostrando também as suas posições na lista.

    Na opção Eliminar aluno, deve ser possível remover um registo com base na posição indicada pelo utilizador.

Validações necessárias:

    A posição deve ser um número inteiro válido e existente na lista.

Após cada operação, o programa d


Critérios de avaliação (4 pontos no total):
(2 pontos) Utilização de funções para organização e reutilização do código.
(1 ponto) Aplicação de boas práticas e normas de programação.
(1 ponto) Implementação de tratamento de exceções e validações para entradas inválidas.


add aluno
Listar alunos
pesquisa alunos
remover aluno

    validar nome
        nao pode ser so espaços
        nao pode ser ""
validar turma
validar se nome e turma na turma


"""

lista_alunos = ["Joao", "Joao", "Maria","Rita"]
lista_turmas = ["1ºA", "2ºA", "1ºA", "1ºA"]
lista_turmas_validas = ["1ºA", "2ºB", "3ºC"]

def all_vals(elm:str, lst:list):
    lista_idx = []
    for index, valor in enumerate(lst):
        if elm == valor:
            lista_idx.append((index, valor))

    return lista_idx



def valTruma(turma:str):
    return turma in lista_turmas_validas

def valNome(nome:str):
    if nome == "":
        return False

    if nome.count(" ") == nome.__len__():
        return False

    return True


def val_is_unique(nome:str, turma:str):

    for idx in all_vals(turma, lista_turmas):
        if lista_alunos[idx[0]] == nome:
            return False
    return True


def addAluno(nome:str, turma:str):
    if (valTruma(turma) and valNome(nome)) and val_is_unique(nome, turma):
            lista_alunos.append(nome)
            lista_turmas.append(turma)
            return True

    return False



def removeAluno(idx:int):
    if type(idx) != int:
        return False

    if idx not in range(len(lista_alunos)):
        return False

    lista_alunos.pop(idx)
    lista_turmas.pop(idx)
    return True

"""
target = 1 -> pesquisar na turma
target = 2 -> pesquisar nos alunos

"""
def find_elm(txt:str, target:int):
    if target == 1:
        return all_vals(txt, lista_alunos)

    elif target == 2:
        return all_vals(txt, lista_turmas)
    else:
        print("target invalido")




print(find_elm("1ºA", 1))
print(find_elm("1ºA", 2))
print(find_elm("Joao", 1))
print(find_elm("Joao", 2))