#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# #dólares ela pode comprar.
n = float(input('Quanto dinheiro você tem na carteira? R$ '))
n1 = float(input('Qual o valor do dolar atualmete? US$ '))
print('Você tem R${:.2f} e pode comprar US${:.2f} dolares.'.format(n, (n / n1)))