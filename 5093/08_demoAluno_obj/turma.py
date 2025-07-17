from dataclasses import dataclass

@dataclass
class Turma:
    id: int
    nome: str
    lista_alunos = []

    def add_aluno(self, aluno):
        self.lista_alunos.append(aluno)