
# loops

# for

#range

"""

range(m) -> todos os num int de 0 ate m-1 <-> range(5) -> [0 1 2 3 4]
                                              range(0,5)

range(n, m) -> todos os num int de n ate m-1 <-> range(3,8) -> [3 4 5 6 7]



range(n, m, s) -> todos os num int de n ate m-1 com um step de s <->
                    range(5,30, 5) -> [5, 10, 15, 20, 25]

"""

# escreve no ecrã a meg "ola mundo" 10 vezes
for i in range(10):
    print(f"Ola Mundo - {i+1} ")

# while

# pede um num ate ser inserido um valor negativo, sempre que o valor for positivp
# mostra o valor inserido


while True:

    try:
        num = int(input("digite um numero: "))
        if num < 0:
            break

    except ValueError:
        print("numero invalido")
        continue

    print(f"o numero digitado foi {num}")

print("o loop terminou")



print("--" * 10)



while int(input("digite um numero: ")) > 0:
    print("o loop esta a correr")

print("o loop terminou")


# listas




# set

# dict

# func