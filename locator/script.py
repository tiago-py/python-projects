import os 
import time 

carros = [
('Honda Civic SI',250),
('Mazda RX-7',400),
('Lancer EVO X',270),
('Golf GTI',200),
('Nissan gtr-r34',350),
('Silvia s15',450)
]
alugados = []

print("=============")
print("Bem vindo a nossa locadora")
print("=============")
time.sleep(1)

def mostrarCarros(carros):
    for i, car in enumerate(carros):
        print("[{}], {} - R$ {}/dia".format(i, car[0],car[1]))


while True:
   
            os.system("cls")
            print("Escolha o que Deseja fazer: ")
            print("[0]->Mostrar lista de carros, [1]->Alugar um carro, [2]->Devolver um carro, [3]->Sair")
            resp = int(input())
            if resp == 3:
                break
            elif resp == 0:
                mostrarCarros(carros)
            
            elif resp == 1:
                mostrarCarros(carros)
                print("Digite o código do carro que deseja alugar: ")
                codigo = int(input())
                print("Por quantos dias você quer alugar este carro?")
                dias = int(input())
                os.system("cls")
                print("O valor total do aluguel ficaria em {} reais".format(carros[codigo][1]*dias))
                print("Você está prestes a alugar o {} por {} dias, deseja confirmar?[0]SIM|[1]NÃO".format(carros[codigo][0],dias))
                conf = int(input()) 
                if conf == 0:
                    print("Você acabou de alugar {} por {} dias, parabéns!!".format(carros[codigo][0],dias))
                    alugados.append(carros.pop(codigo))
                else:
                    print("Voltando ao inicio")
            elif resp == 2:
                if len(alugados) < 0:
                    print("Não há carros para devolver")
                else:
                    mostrarCarros(alugados)
                    print("Digite o codigo do carro que deseja devolver:")
                    codigo02 = int(input())
                    print("")
                    carros.append(alugados.pop(codigo02))
                    os.system("cls")
                    print("Obrigado por devolver o carro, volte sempre")

            print("Deseja continuar? [0]SIM|[1]NÃO")
            resp02 = int(input())
            if resp02 == 1:
                break
            
