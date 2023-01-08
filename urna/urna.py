import time 
lula = 0
bolsonaro = 0
bocaDe09 = 0
fulanoDeTal = 0
ciclano = 0
eleitor = 0

    
print('Digite seu voto para Presidente: ')
print('Opções: ')
print('===========')
print('Lula = L')
print('Bolsonaro = B')
print('Boca de 09 = 09')
eleitor = input(' ').upper

print('Digite seu voto para Deputado: ')
print('Opções: ')
print('===========')
print('Fulano de tal = F')
print('Ciclano = C')

eleitor = input(' ').upper


if eleitor == 'L':
  lula += 1
elif eleitor == 'B':
  bolsonaro += 1
elif eleitor  == '09':
  bocaDe09 += 1
else:
  print('')
if eleitor == 'F':
  fulanoDeTal += 1
elif eleitor == 'C':
  ciclano += 1

print('Contando votos...')
time.sleep(1)

if lula > bolsonaro and lula > bocaDe09:
  print('Lula venceu a eleição para Presidente do Brasil')
  print('VIVA O COMUNISMO')
elif bolsonaro > lula and bolsonaro > bocaDe09:
  print('Bolsonaro venceu a eleição para Presidente do Brasil')
else:
  print('Boca de 09 GANHOOOOOOO')


print('Contando os votos para Deputados...')
time.sleep(1)

if fulanoDeTal > ciclano:
  print('Fulano de tal venceu')
else:
  print('Ciclano venceu')

