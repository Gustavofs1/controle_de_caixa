from src import *
import os

os.system('cls')

while True:
    menu()
    opcao = int(input())
    if opcao == 1:                                #OPÇÃO ABERTURA DO CAIXA
        adiciona_produto(pedido_novo=True)
    elif opcao == 2:                              #OPÇÃO VENDAS
        adiciona_produto(pedido_novo=False)
    elif opcao == 3:                              #OPÇÃO FECHAMENTO DE CAIXA
        fechar_caixa()
    elif opcao == 4:                              #OPÇÃO ENTRADA
        tela_entrada()
    elif opcao == 5:                              #OPÇÃO SAIDA
        tela_saida()
    elif opcao == 6:                              #CLOSE SYSTEM
        break