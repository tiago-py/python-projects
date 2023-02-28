import random 

bot = random.randint(1,100)
print("================")
print("Bem vindo ao jogo de advinha!! Adivinhe o número que o computador pensou(DE 1 A 100)")
print("================")

for i in range(10):
    print("Digite um número:")
    resp = int(input())
    if bot > resp:
        print("Errou, o número é maior!!")
    elif bot < resp:
        print("Errou, o número é menor!!")
    else:
        print("Acertou")        