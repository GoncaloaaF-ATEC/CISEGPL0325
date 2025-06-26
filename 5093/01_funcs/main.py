#pip install numpy
import numpy as np

"""

var
loops - for e while
condições - if e match
Collections
    list -> [] <-
    dict -> {k:v}
    set -> {}

"""


nomes = ["nome 1", "nome 2", "nome 3", "nome 4"]
print(nomes)
print(len(nomes))
print(nomes[3])

nomes.append("nome 5") # add no final
print(nomes)
print(len(nomes))

nomes.insert(2, "nome 6")
print(nomes)
print(len(nomes))

nomes.insert(0, "nome 6")
print(nomes)
print(len(nomes))

nomes.remove("nome 6") # "nome 6" tem de existir na lista
print(nomes)
print(len(nomes))



nomes.pop()
print(nomes)
print(len(nomes))



nomes2 = ["nome 3", "nome 1", "nome 3", "nome 2", "nome 3", "nome 4", "nome 3"]
print(nomes2)

todel = "nome 3"
while todel in nomes2:
    nomes2.remove(todel)

print(nomes2)



mat = [[0,1,2],
       [3,4,5],
       [6,7,8]]


mat2 = [[10,11,12],
       [13,14,15],
       [16,17,18]]



print("-------------------------------")

np_mat = np.array(mat)
np_mat2 = np.array(mat2)

np_mat_times = np_mat * 2

print(np_mat_times)
print("-------------------------------")

np_mat_sum = np_mat + np_mat2

print(np_mat_sum)


