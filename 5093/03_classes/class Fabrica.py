from dataclasses import dataclass
from Cliente import Cliente

@dataclass
class Fabrica:

    lista_clientes: list[Cliente]

    def add_cliente(self, cliente: Cliente):
        self.lista_clientes.append(cliente)