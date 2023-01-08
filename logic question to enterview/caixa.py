import time 
import random

alto = 1000
medio = 100
baixo = 0
gat = 0

  
caixa = baixo


if caixa == baixo:
  caixa = medio
  print(f'Caixa no nivel baixo, {baixo} ML')
  print('Enchendo a caixa ')
  time.sleep(3)
if caixa == medio:
  caixa = alto
  print(f'Caixa no nivel médio, {medio} ML')
  print('Enchendo a caixa novamente')
  time.sleep(5)
if caixa == alto:
 caixa = gat
 print(f'Caixa no nivel alto, {alto} ML')

 time.sleep(5)
for i in range(1,100):
  if caixa == gat:
     caixa = random.choice(medio, alto)
  if caixa == baixo:
    caixa = medio
    print(f'Caixa no nivel baixo, {baixo} ML')
    print('Enchendo a caixa ')
  
  if caixa == medio:
    caixa = alto
    print(f'Caixa no nivel médio, {medio} ML')
    print('Enchendo a caixa novamente')
  if caixa == alto:
   caixa = gat
   print(f'Caixa no nivel alto, {alto} ML')
  
   time.sleep(5)