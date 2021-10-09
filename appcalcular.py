print('======================= SIMULADOR =======================')
valor = float(input('Valor do veículo ou imóvel: '))
porcento = int(input('Porcentagem % : '))
entrada = float(input('Valor da entrada : '))
parcelas = int(input('Valor das parcelas: '))
n1 = valor + (valor * porcento /100)
n2 = (n1 - entrada) / parcelas
print('======================= RESULTADO DA SIMULAÇÃO DE PROPOSTA =======================')
print('Valor solicitado: {:.2f}'
      '\nPorcentagem de: {}%'
      '\nEntrada de: {:.2f}'
      '\nParcelas no valor de: {:.2f}'.format(valor, porcento, entrada, parcelas))
print('Resultado do cálculo:   {}'.format(n1))
print('O Total das parcelas é: {:.2f} vezes de: {}'.format(n2, parcelas))
#print('O resultado da proposta é: {} '.format(n1, n2))