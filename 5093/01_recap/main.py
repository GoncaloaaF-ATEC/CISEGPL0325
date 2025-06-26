from Aluno import Aluno

# cmt

"""
cmt
multi
linha

"""


# var



# condições



# loops

# range(N, M, S) -> vai de N a M-1 com step de S

for i  in range(10):
    print(i, end=" ")

print()
for i  in range(5, 10):
    print(i, end=" ")

print()

for i  in range(7, 50, 5):
    print(i, end=" ")

print()
print("----")
print(i)


i = 0
j = 5
while i < 5 and j < 15:
    i += 1
    j += i

    for elm in range(i, j):
        print(f"{i}-{j} -> ", end=" ")
        print(elm)


    # RSA ->
    # 10 % 2 <- resto da div inteira
    # 6 Mod 5  1 2 3 4 0 1


print("fim do while")

# listas

# list

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(mylist[0:5])

print(mylist[4:8])

print(mylist[1:12:4])

print(mylist[::-2])

#  mylist[a]  -> a = index (se for neg conta do fim)

# list slice
#  mylist[n:m] -> n 1º valor do slice, m-1 ultimo valor do slice

#  mylist[n:m:s] -> n 1º valor do slice, m-1 ultimo valor do slice, s -> Step (qts val salta)

#  mylist[::s] -> do 1º da lista ate ao ultimo, s-> Step (qts val salta), se for neg inverte a lista


#print(mylist[-1:-5:-1])



print(len(mylist))

print(mylist.__len__())

#help(int)

r = mylist[-1]

print(mylist)
mylist.append(99) ## add no final
print(mylist)

mylist.insert(2, 999) # mylist.insert(2, 999)
print(mylist)


while False:
    val = int(input("digite um valor: "))
    pos = int(input("digite um index: "))
    mylist.insert(pos, val) # mylist.insert(2, 999)

    nxt = input("sair(s/n)?: ")
    if nxt.lower() == "s":
        break



mylist[0] = None
print(mylist)


lista = []
for _ in range(10):
    lista.append(None)

print(lista)


lista.insert(2, 999)
print(lista)
lista[0] = 123
print(lista)


n = 100000000000000
n2 = 100_000_000_000_000
n3= 10_000_000_000

print(n2 / 10_000)


print(19 in lista)
lista.append(19)

print(19 in lista)

print(lista.__contains__(19))

# mylist.remove(19)
# mylist.pop()
# mylist.pop(2)
# set


myset = {1,2,3,4,5,6}

print(myset)

myset.add(7)

print(myset)

myset.add(7)

print(myset)

print(myset.remove(7)) # o val tem de existir

print(myset)

print(myset.discard(77))

print(myset)

myset.pop()
print(myset)



set1 = {"Farinha", "Ovos", "Açucar", "Oleo", "iogurte"}

set2 = {"Polvilho", "Ovos", "sal", "Oleo", "Leite", "Queijo"}

print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.union(set2))

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.__len__())

set1.difference_update(set2) # <=> set1 = set1.difference(set2)


for elm in set1:

    print(elm, end=" ")

print("")
# dict

my_dict = {"key": "value",
           "key2": "value2",
           "key3": "value3"}


print(my_dict["key"])

print(my_dict.get("key11"))


my_dict["key11"] = "Novo valor"
print(my_dict.get("key11"))

# del my_dict["key16"]
# my_dict.pop("key16")


#my_dict.clear()

#print(my_dict)


print(my_dict.keys().__contains__("key11"))

print(my_dict.values())

print(list(my_dict.keys())[0])

print("---" * 5)
for elm in my_dict:
    print(elm, end=" ")
print()

print("---" * 5)
for elm in my_dict.keys():
    print(elm, end=" ")
print()

print("---" * 5)
for elm in my_dict.values():
    print(elm, end=" ")
print()


print("---" * 5)
for elm in my_dict.items():
    print(elm, end=" ")
print()


cod = [5093]
nome = ["Estruturas de dados compostas"]
ufcd = {5093:"Estruturas de dados compostas"}


usrList = {"Aluno1": Aluno("nome Aluno", "Ciber"),
           "Aluno2": Aluno("nome Aluno2", "Ciber")}


print(usrList)

