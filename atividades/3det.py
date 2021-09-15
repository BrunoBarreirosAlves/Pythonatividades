from time import time

import listas as listas
import timer as timer
produto = 0
preco = 0
quantidade = 0

print("====================================== BAZAR DA IRACEMA========================================")
print("  ******   ***********    **********     *********   **********   ***       ***   *********** ")
print("    **     ***     ****   **********    **********   **********   ****     ****   *********** ")
print("    **     ***     ****   ***    ***   ***           ***          *************   ***     *** ")
print("    **     ***    ****    ***    ***   ***           ***          ***  ***  ***   ***     *** ")
print("    **     **********     **********   ***           *********    ***   *   ***   *********** ")
print("    **     ***    ***     **********   ***           ***          ***       ***   *********** ")
print("    **     ***     ***    ***    ***    ***          ***          ***       ***   ***     *** ")
print("    **     ***      ***   ***    ***     *********   **********   ***       ***   ***     *** ")
print("  ******   ***       ***  ***    ***      ********   **********   ***       ***   ***     *** ")


#print('===================================== PRODUTOS ==========================================')

lista_produto = ["VESTIDO     ", "SAIA        ", "SHORT JEANS ", "CALÇA JEANS ", "CAMISA      ", "SAPATO      ", "SANDALIA    ", "PERCATA     ", "BLUSÃO      ", "BIJUTERIAS  ", "VARIEDADES  ", "SAPATO      ", "PERCATA     ", "BOTA        ", "BIQUINES    ", "SUNGAS      ", "MEIA        ", "BOLSA       ", "TOLCA       ", "BONÉ        ", "CD          ", "DVD         ", "Lanches     ", "Bebidas     "]

#print('===================================== QUANTIDADE=========================================')
lista_quantidade = ['50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50', '50']

#print('===================================== PREÇO ==========================================')
lista_preco = [" R$ 5,00", " R$ 1,00", " R$ 2,00", " R$ 3,00", " R$ 2,00", " R$ 1,00", " R$ 1,00", " R$ 1,00", " R$ 1,00", " R$ 1,00", " R$ 5,00", " R$ 1,00", " R$ 2,00", " R$ 3,00", " R$ 2,00", " R$ 1,00", " R$ 1,00", " R$ 1,00", " R$ 1,00", " R$ 5,00", " R$ 1,00", " R$ 1,00", " R$ 3,00 ", "R$ 5,00"]


while True:
    print('===================================== MENU ==========================================')
    print("[ 1 ] - Cadastrar produto")
    print("[ 2 ] - Lista de produtos Cadastrados")
    print("[ 3 ] - Catalogo de roupas")
    print("[ 4 ] - Sair")

    op = int(input("DIGITE A OPÇÃO : "))#Escolha da opcao

    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        #id = input("Id da pessoa")
        produto = input("Nome do produto: ")
        #nome = input("Digite o nome da pessoa")
        quantidade = input("Quantidade do produto: ")
        #idade = input("Idade da pessoa")
        preco = input("Valor unitário: ")
        nova.insert(lista_produto)
        nova.insert(lista_quantidade)
        nova.insert(lista_preco)
        listas.insert()#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    if op == 2:
        print('===================================== PRODUTOS CADASTRADOS ==========================================')
        listas.append(lista_produto, lista_quantidade, lista_preco)
        print("Produto: ", produto, "Quantidade: ", quantidade, "Unidades", 'Preço', preco)

    if op == 3:
         print('======================================== CATÁLOGO DE ROUPAS =========================================')
         print("Produto:  ",  lista_produto[0], "  Quantidade: ",  lista_quantidade[0], "Unidades ", '  Preço', lista_preco[0])
         print("Produto:  ",  lista_produto[1], "  Quantidade: ",  lista_quantidade[1], "Unidades ", '  Preço', lista_preco[1])
         print("Produto:  ",  lista_produto[2], "  Quantidade: ",  lista_quantidade[2], "Unidades ", '  Preço', lista_preco[2])
         print("Produto:  ",  lista_produto[3], "  Quantidade: ",  lista_quantidade[3], "Unidades ", '  Preço', lista_preco[3])
         print("Produto:  ",  lista_produto[4], "  Quantidade: ",  lista_quantidade[4], "Unidades ", '  Preço', lista_preco[4])
         print("Produto:  ",  lista_produto[5], "  Quantidade: ",  lista_quantidade[5], "Unidades ", '  Preço', lista_preco[5])
         print("Produto:  ",  lista_produto[6], "  Quantidade: ",  lista_quantidade[6], "Unidades ", '  Preço', lista_preco[6])
         print("Produto:  ",  lista_produto[7], "  Quantidade: ",  lista_quantidade[7], "Unidades ", '  Preço', lista_preco[7])
         print("Produto:  ",  lista_produto[8], "  Quantidade: ",  lista_quantidade[8], "Unidades ", '  Preço', lista_preco[8])
         print("Produto:  ",  lista_produto[9], "  Quantidade: ",  lista_quantidade[9], "Unidades ", '  Preço', lista_preco[9])
         print("Produto:  ", lista_produto[10], "  Quantidade: ", lista_quantidade[10], "Unidades ", '  Preço', lista_preco[10])
         print("Produto:  ", lista_produto[11], "  Quantidade: ", lista_quantidade[11], "Unidades ", '  Preço', lista_preco[11])
         print("Produto:  ", lista_produto[12], "  Quantidade: ", lista_quantidade[12], "Unidades ", '  Preço', lista_preco[12])
         print("Produto:  ", lista_produto[13], "  Quantidade: ", lista_quantidade[13], "Unidades ", '  Preço', lista_preco[13])
         print("Produto:  ", lista_produto[14], "  Quantidade: ", lista_quantidade[14], "Unidades ", '  Preço', lista_preco[14])
         print("Produto:  ", lista_produto[15], "  Quantidade: ", lista_quantidade[15], "Unidades ", '  Preço', lista_preco[15])
         print("Produto:  ", lista_produto[16], "  Quantidade: ", lista_quantidade[16], "Unidades ", '  Preço', lista_preco[16])
         print("Produto:  ", lista_produto[17], "  Quantidade: ", lista_quantidade[17], "Unidades ", '  Preço', lista_preco[17])
         print("Produto:  ", lista_produto[18], "  Quantidade: ", lista_quantidade[18], "Unidades ", '  Preço', lista_preco[18])
         print("Produto:  ", lista_produto[19], "  Quantidade: ", lista_quantidade[19], "Unidades ", '  Preço', lista_preco[19])
         print("Produto:  ", lista_produto[20], "  Quantidade: ", lista_quantidade[20], "Unidades ", '  Preço', lista_preco[20])
         print("Produto:  ", lista_produto[21], "  Quantidade: ", lista_quantidade[21], "Unidades ", '  Preço', lista_preco[21])
         print("Produto:  ", lista_produto[22], "  Quantidade: ", lista_quantidade[22], "Unidades ", '  Preço', lista_preco[22])

    if op == 4:
        timer = 5
        print(" Saindo...".format(timer) )



