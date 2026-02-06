import numpy as np

state = 'start'
tabuleiro = np.zeros((8, 8))

def start():
    print("Olá! Bem-vindo ao TerminalChess")
    print("1 - Jogador (indisponível)")
    print("2 - Multijogador")
    # Exemplo de impressão individual
    print("\u2654")  # Rei Branco ♔
    print("\u265F")  # Peão Preto ♟

    return input("Selecione o modo: ")

def jogador_1():
    origem = input("Jogador 1 (brancas) selecione uma peça ")
    destino = input("Mova a peça ")

def jogador_2():
    origem = input("Jogador 2 (pretas) selecione uma peça ")
    destino = input("Mova a peça ")

while state != 'finish':
    if state == 'start':
        modo = start()
        while modo != "2":
            print('Não disponível, selecione outro')
            modo = start()

        print(tabuleiro)

        jogador_1()
        jogador_2()
        state = 'finish'

    