#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# #calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.
larg = float(input(' Qual a largura da parede? '))
alt = float(input(' Qual a altura da parede? '))
print(' A sua área é: {} metros quadrados.\n A quantidade de tinta necessária para pintá-la é {}. '.format(larg + alt, (larg + alt )/ 2), '\n Agradecemos a preferencia!')