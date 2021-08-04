#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input(' Digite a distância em metros: '))
cm = n * 100
mm = n * 1000
print(' A distância de {}m corresponde a:'.format(n))
print('{}cm\n{}mm\n'.format(cm, mm))

