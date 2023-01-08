import random 
import time 

number = int(input('Digite um número para o computador advinhar entre 1 e 10!!: '))


guess = 0

while guess != number:
  time.sleep(1)
  guess = random.randint(1,10)
  time.sleep(1)
  if guess < number:
    print(guess)
    print('O computador tentou um número menor que o seu número!!')
  elif guess > number:
    print(guess)
    print('O computador tentou um número maior que o seu número!!')
print('Yay o computador acertou!!!')