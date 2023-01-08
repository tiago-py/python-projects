import random  

ia = random.randint(1,10)

print('A máquina pensou em um número ')
print('     ')

for i in range(1,11):
  
  jogador = int(input('Tente acertar o número que a máquina pensou (numero está entre 1 e 10): '))

  if jogador == ia:
    print('Acertou!!')
    exit()
  elif jogador < ia:
    print('O número que a máquina pensou é maior que', jogador)
  else:
    print('O número que a máquina pensou é menor que', jogador)
  