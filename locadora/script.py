import os
import time

carros = [
    ('Honda Civic SI', 250),
    ('Mazda RX-7', 400),
    ('Lancer EVO X', 270),
    ('Golf GTI', 200),
    ('Nissan GTR R34', 350),
    ('Silvia S15', 450)
]
alugados = []

def mostrar_carros(carros, titulo="Lista de carros disponíveis"):
    print("\n" + titulo)
    for i, (nome, valor) in enumerate(carros):
        print(f"[{i}] {nome} - R$ {valor}/dia")

def alugar_carro():
    mostrar_carros(carros)
    codigo = int(input("Digite o código do carro que deseja alugar: "))
    dias = int(input("Por quantos dias você quer alugar este carro? "))
    total = carros[codigo][1] * dias
    print(f"O valor total do aluguel ficaria em R$ {total}")
    confirmacao = input(f"Você está prestes a alugar o {carros[codigo][0]} por {dias} dias. Deseja confirmar? (s/n): ").strip().lower()
    if confirmacao == 's':
        alugados.append(carros.pop(codigo))
        print(f"Você alugou {carros[codigo][0]} por {dias} dias. Parabéns!")
    else:
        print("Operação cancelada.")

def devolver_carro():
    if not alugados:
        print("Não há carros para devolver.")
    else:
        mostrar_carros(alugados, "Lista de carros alugados")
        codigo = int(input("Digite o código do carro que deseja devolver: "))
        carros.append(alugados.pop(codigo))
        print("Carro devolvido com sucesso!")

def adicionar_carro():
    nome = input("Digite o nome do carro que deseja adicionar: ")
    valor = int(input("Digite o valor do carro que deseja adicionar: "))
    carros.append((nome, valor))
    print("Carro adicionado com sucesso!")

def editar_carro():
    mostrar_carros(carros)
    codigo = int(input("Digite o código do carro que deseja editar: "))
    nome = input("Digite o novo nome do carro: ")
    valor = int(input("Digite o novo valor do carro: "))
    carros[codigo] = (nome, valor)
    print("Carro editado com sucesso!")

def menu():
    print("\nEscolha uma opção:")
    print("[0] Mostrar lista de carros")
    print("[1] Alugar um carro")
    print("[2] Devolver um carro")
    print("[3] Adicionar um carro")
    print("[4] Editar um carro")
    print("[5] Sair")
    return int(input("Opção: "))

def main():
    print("=============")
    print("Bem-vindo à nossa locadora")
    print("=============")
    time.sleep(1)

    while True:
        opcao = menu()

        if opcao == 0:
            mostrar_carros(carros)
        elif opcao == 1:
            alugar_carro()
        elif opcao == 2:
            devolver_carro()
        elif opcao == 3:
            adicionar_carro()
        elif opcao == 4:
            editar_carro()
        elif opcao == 5:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == '__main__':
    main()
