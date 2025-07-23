brands = []
models = []
import msvcrt as m  # getche do c
import os


def wait():
    print("Clique em qualquer tecla para continuar...")
    m.getch()


def clear():
    os.system('cls')


def main():
    while True:
        print("Bem-vindo ao stand do Boda!")
        print("Por favor, escolha uma opção: ")
        print("1 - Adicionar um carro ")
        print("2 - Remover um carro ")
        print("3 - Pesquisar ")
        print("4 - Sair do Programa")

        option = int(input())

        match option:
            case 1:
                while len(brands) < 100:
                    brand = input("Qual é a marca do carro?\n")
                    brands.append(brand)
                    print(brands)
                    model = input("Qual é o modelo?\n")
                    models.append(model)
                    print(models)
                    rollback = input("Veículo adicionado à lista, pretende adicionar outro? (Y/N)")
                    if rollback.upper() == 'Y':
                        continue
                    elif rollback.upper() == 'N':
                        break
                if len(brands) == 100:
                    print("Capacidade máxima alcançada.")
                    wait()
                    clear()
                    continue
            case (2):
                if len(brands) == 0:
                    print("A lista está vazia Zeca!\n Clique em qualquer tecla para continuar...")
                    wait()
                    clear()
                    continue
                else:
                    print("Lista dos veiculos disponiveis:\n")
                    for i in range(0, len(brands)):
                        print(f"{brands[i]} {models[i]} - {i}")
                    delete = int(input(
                        "Qual é o carro que deseja remover? (utilize os numeros referidos abaixo da marca/modelo)\n\n"))
                    brands.pop(delete)
                    models.pop(delete)
                    print("Carro foi removido da base de dados.")
                    wait()
                    clear()
                    continue
            case 3:  # search
                search = input("Deseja procurar através da marca ou do modelo?")
                if search.lower() == 'marca':
                    search2 = input("Qual é a marca do veiculo?")
                    searchbar = []
                    for i in range(0, len(brands)):
                        if brands[i] == search2:
                            searchbar.append((models[i], i))

                    for s in searchbar:
                        print(s, end=";\n")
                    wait()
                    clear()
                    continue
                else:
                    if search.lower() == 'modelo':
                        search2 = input("Qual é o modelo do veiculo?")
                        searchbar = []
                        for i in range(0, len(models)):
                            if models[i] == search2:
                                searchbar.append(i)
                            searchbar.append((brands[i], i))
                        for s in searchbar:
                            print(s, end=";\n")
                        wait()
                        clear()
                        continue
            case (4):
                print("A sair do programa, obrigado pela visita! ")
                break


main()
