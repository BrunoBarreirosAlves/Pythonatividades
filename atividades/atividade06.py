#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print("Analisando o número [ {} ]\nO seu dobro é: [ {} ]\nSeu triplo é: [ {} ]\nE sua raiz quadrada é: [ {:.2f} ]\n".format(n, (n * 2 ), (n * 3), (n ** ( 1 / 2))))