#Ajudem a passar no teste 13 Segue meu codigo
from tkinter import font

import timer as timer

tempo_segundo = 0
if timer < 20:
    timer += 1

else:
    tempo_segundo += 1
    texto = font.render(' Luiza: ' + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
    timer = 0
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(timer, tempo_segundo))