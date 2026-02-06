import numpy as np

state = 'start'
tabuleiro = np.zeros((8, 8))

def start():
    print("Olá! Bem-vindo ao TerminalChess")
    print("1 - Jogador (indisponível)")
    print("2 - Multijogador")
    return input("Selecione o modo: ")


while state != 'finish':
    if state == 'start':
        modo = start()
        while modo != "2":
            print('Não disponível, selecione outro')
            modo = start()

        print(tabuleiro)
        state = 'finish'

    