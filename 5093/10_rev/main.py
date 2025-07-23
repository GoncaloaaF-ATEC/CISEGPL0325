

lst = [
    "Diogo", "Miguel", "Inês", "Tiago", "Sofia", "João",
    "Mariana", "Diogo", "Beatriz", "Rodrigo", "Matilde",
    "Rafael", "Leonor", "Guilherme", "Lara", "Tomás",
    "Carolina", "Afonso", "Madalena","Diogo", "Henrique", "Francisca",
    "Martim", "Ana", "Diogo", "Pedro", "Catarina", "Vasco"
]

lst2 = [
    "Diogo", "Miguel", "Inês", "Tiago", "Sofia", "João",
    "Mariana", "Diogo", "Beatriz", "Rodrigo", "Matilde",
    "Rafael", "Leonor", "Guilherme", "Lara", "Tomás",
    "Carolina", "Afonso", "Madalena","Diogo", "Henrique", "Francisca",
    "Martim", "Ana", "Diogo", "Pedro", "Catarina", "Vasco","Diogo"
]


nome = "Diogo"
lista_pos = []

num = lst.count(nome) # num de elm

#print(lst.index(nome))

# print(lst.index(nome))
# print(lst.index(nome, 7))
# print(lst.index(nome, 19))
# print(lst.index(nome, 24))


for _ in range(num):
    if lista_pos.__len__() == 0:
        lista_pos.append(lst.index(nome))
        continue

    lista_pos.append(lst.index(nome, lista_pos[-1] + 1))


print(lista_pos)


for i in lista_pos:
    print(i, "- ", lst2[i], end=";\n")




#for valor in enumerate(lst):
#    print(f"idx {valor[0]} - {valor[1]}")



nome = "Diogo"

idx = lst2.index(nome)
print(lst2[idx])