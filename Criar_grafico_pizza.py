#GRÁFICOS DE PIZZA

import matplotlib.pyplot as plt
import numpy as np

#Colocando valores
valor = np.array([25, 20, 30, 25])

#produtos
mylabels = ['Saia', 'Short', 'Calça', 'Sapato']

#Espaço entre os gráficos
myexplode = [0.3, 0.1, 0.1, 0.1]

#Cria o gráfico e mostra na tela
plt.pie(valor, labels=mylabels, explode=myexplode, shadow=True)
plt.show()


