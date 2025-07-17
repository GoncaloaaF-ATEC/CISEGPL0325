"""

Na opção Registar novo aluno, o utilizador deve poder adicionar o nome do aluno e a turma,
 respeitando o limite máximo de 100 registos.

1. Validações necessárias:
1. O nome do aluno não pode estar vazio nem conter apenas espaços.
2. A turma deve ser um valor válido (exemplo: "1.°A", "2.°B", "З.°C, pode definir quais turmas são válidas).
3. Não deve permitir registo duplicado do mesmo aluno na mesma turma.


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

def all_index(elm:str, lst:list):
    lista_idx = []
    for index, valor in enumerate(lst):
        if elm == valor:
            lista_idx.append(index)

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

    for idx in all_index(turma, lista_turmas):
        if lista_alunos[idx] == nome:
            return False
    return True


def addAluno(nome:str, turma:str):
    if (valTruma(turma) and valNome(nome)) and val_is_unique(nome, turma):
            lista_alunos.append(nome)
            lista_turmas.append(turma)

"""
target = 1 -> pesquisar na turma
target = 2 -> pesquisar nos alunos

"""
def findAluno(txt:str, target:int):
    pass



print(val_is_unique("Joao", "1ºA"))
print(val_is_unique("Joao", "2ºA"))
print(val_is_unique("Joao", "5ºA"))