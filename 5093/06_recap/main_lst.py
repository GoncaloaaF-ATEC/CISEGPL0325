lst = [12,41,4,12,3,523,12,3,1,1223,12]

print(lst)

lst.append(999)

print(lst)

#lst.append(int(input("insira um valor: ")))


print(lst)

lst2 = [12.1,2,31, True, "Ola mundo"] #<- evitar

print(lst2)


print(lst)

lst[0] = 99_999
print(lst)

print(int("99_999"))

int64max = 9223372036854775807

print(f"{int64max}")
print(f"{int64max:b}")
print(f"{int64max:o}")
print(f"{int64max:_}")

print()


lst.insert(0, 111111)
print(lst)

lst.insert(348723, 888888)
print(lst)


print(lst.index(888888))


lst.insert(-1, 556677)



print(lst[-1])

print(lst.pop())

print(lst)


print(lst.pop(0))

print(lst)

print(lst.remove(41))

print(lst)