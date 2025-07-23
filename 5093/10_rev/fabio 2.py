brands = []
models = []


search2 = "BMW"
searchbar = [] #res pesquisa

ct = brands.count(search2)

for i in range(len(brands)):
    if brands[i] == search2:
            searchbar.append((models[i], i))

for s in searchbar:
    print(s, end=";\n")
