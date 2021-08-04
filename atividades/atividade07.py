#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input(' Digite a primeira nota: '))
n2 = float(input(' Digite a segunta nota: '))
n3 = float(input(' Digite a terceira nota: '))
n4 = float(input(' Digite a quarta nota: '))

print(' Sua média de notas é: {:.1f}'.format((n1 + n2 + n3 + n4) /4))