nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Gabriela", "Hugo",
    "Inês", "João", "Karina", "Luís", "Mariana", "Nuno", "Olívia", "Paulo",
    "Quésia", "Rui", "Sofia", "Tiago", "Úrsula", "Vítor", "Wanda", "Xavier",
    "Yara", "Zé", "Beatriz", "Cláudio", "Diana", "Emanuel", "Fábio", "Graça",
    "Helena", "Igor", "Jéssica", "Leandro", "Marta", "Natália", "Oscar", "Patrícia"
]

print(len(nomes))

print(nomes.__len__())


print(nomes[2:10]) # ['Carla', 'Daniel', 'Eduarda', 'Fernando', 'Gabriela', 'Hugo', 'Inês', 'João']

print(nomes[2:10:2]) # ['Carla',  'Eduarda' , 'Gabriela', 'Inês' ]

print(nomes[::-5])


msg = "ola Mundo"

print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.swapcase())
print(msg.title())

for elm in enumerate(nomes):
    print(elm)

print("-----" * 10)
print(list(enumerate(nomes)))

print("-----" * 10)




