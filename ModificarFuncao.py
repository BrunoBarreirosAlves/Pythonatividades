#Modificar comportamento de funcao sem alterá-la

import time
#Decorator
def calcula_duracao(funcao):
    def wrapper():
        #calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_total = str(time.time() - tempo_inicial)

        print(f'[{funcao.__name__}] Duração: {tempo_total}')

     return wrapper
#Calcula_duracao
def main():
    for n in range(0.10000000):
        pass

# Chama a função
main()















