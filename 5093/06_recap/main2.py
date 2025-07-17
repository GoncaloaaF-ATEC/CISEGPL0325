print("--" * 10,"continue", "--"* 10)

for i in range(20):
    if i % 2 == 0:
        pass

    print(f"{i:2}", end=" ")

print("")
for i in range(20):
    if i % 2 == 0:
        continue

    print(f"{i:2}", end=" ")


print("----"*10)

for i, elm in enumerate(range(2,20, 4)):
    print(f"volta: {i}, valor: {elm}")


print("----"*10)

count = 0
for elm in range(2,20, 4):
    print(f"volta: {count}, valor: {elm}")
    count += 1