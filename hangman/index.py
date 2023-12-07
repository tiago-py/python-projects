import random

words = ["carro", "aviao", "moto", "casa"]
word = random.choice(words)
lifes = 10
responses = ''
while lifes > 0:
    failed = 0
    for char in word:
        if char in responses:
            print(char, end=""),
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print(" ")
        print(f"Você venceu, a palavra era : {word}")
        break
    
    print(f"  Adivinhe a palavra você tem {lifes} vidas restantes!!")
    response = input()
    responses += response

    if response not in word:
        print("Errou!")
        print("_", end="")
        lifes -= 1
        if lifes <= 3:
            print(" ")
            print("Cuidado suas vidas estão acabando!!")
    if lifes == 0:
        print("Perdeu")
        break