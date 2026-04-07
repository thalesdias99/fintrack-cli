gastos = []

def adicionar_gasto(nome, valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos.append({"nome": nome, "valor": valor})

def listar_gastos():
    return gastos

def total_gastos():
    return sum(g["valor"] for g in gastos)

def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            valor = float(input("Valor: "))
            adicionar_gasto(nome, valor)

        elif op == "2":
            for g in listar_gastos():
                print(g)

        elif op == "3":
            print("Total:", total_gastos())

        elif op == "4":
            break

if __name__ == "__main__":
    menu()