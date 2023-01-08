#gerador de senhas simples usando python

#importar a biblioteca random
import random


#carácteres e numeros para a senha

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = '1234567890'
special = '!@#$%&*:?!'
all = lower + upper + numbers + special
#definir o tamanho e a quantidade de senhas geradas

tamanho = int(input('Digite a quantidade de caracteres da senha que deseja gerar: '))
quant = int(input('Digite a quantidade de senhas que deseja gerar: '))


#definindo o loop para a senha

for i in range(quant):
  password = ''
  for g in range(tamanho):
    password = ''.join([password, random.choice(all)])
    
print(password)
    
  