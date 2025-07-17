from dataclasses import dataclass

@dataclass
class Escola:
    lista_turmas = []


    def val_turma(self, turma):
        return not turma in self.lista_turmas


    def adicionar_turma(self, turma):
        if self.val_turma(turma):
            self.lista_turmas.append(turma)


    def adicionar_Aluno(self, aluno, turma):
        idx = self.lista_turmas.index(turma)

        if turma:
            self.lista_turmas[idx].add_aluno(aluno)