"""

 clientes
  compras por eles efetuadas(

   Númcli(Automático), NomCli, morada, tel, nif, , Divfin ).

"""

from dataclasses import dataclass

@dataclass
class Cliente:
    Numcli:int
    nomCli:str
    morada:str
    tel:str
    nif:str
    compras:str
    divfin:str






