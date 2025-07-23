
lst = []
dict = {"key":"value"}
mySet = {}

lst = [
    "Diogo", "Miguel", "Inês", "Tiago", "Sofia", "João",
    "Mariana", "Diogo", "Beatriz", "Rodrigo", "Matilde",
    "Rafael", "Leonor", "Guilherme", "Lara", "Tomás",
    "Carolina", "Afonso", "Madalena","Diogo", "Henrique", "Francisca",
    "Martim", "Ana", "Diogo", "Pedro", "Catarina", "Vasco","Diogo"
]

cliente = {
    "nome": "nome 1",
    "morada": "nome 1",
    "telefone": "telefone 1",
    "nif": "nif 1",
    "compra": "compra 1",
    "divida": "divida 1",
}

cliente2 = {
    "nome": "nome 2",
    "morada": "nome 2",
    "telefone": "telefone 2",
    "nif": "nif 2",
    "compra": "compra 2",
    "divida": "divida 2",
}

cliente3 = {
    "nome": "nome 3",
    "morada": "nome 3",
    "telefone": "telefone 3",
    "nif": "nif 3",
    "compra": "compra 3",
    "divida": "divida 3",
}

lst2 = [cliente, cliente2, cliente3]

print(lst2)

nome = "nome 1"

for clt in lst2:
    if clt["nome"] == nome:
        print(clt["nome"])
        print(clt["morada"])
        print(clt["telefone"])
        print(clt["compra"])







