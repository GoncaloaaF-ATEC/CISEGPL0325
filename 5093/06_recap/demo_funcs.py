
def my_func():
    print("hello")


my_func()
my_func()

# hint
def soma(n1:float, n2:float):
    soma3 = n1 + n2
    print(soma3)


soma(3.1, 4.1)
soma(3, 4)

def soma4(n1:float, n2:float):
    soma2 = n1 + n2
    return soma2


res = soma4(3.1, 4.1)

print(res)

print(soma4(3.2, 4.2))