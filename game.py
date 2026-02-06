import numpy as np
from tabuleiro import ChessBoard

state = 'start'
tabuleiro = ChessBoard()

def start():
    print("Olá! Bem-vindo ao TerminalChess")
    print("1 - Jogador (indisponível)")
    print("2 - Multijogador")
    # Exemplo de impressão individual
    print("\u2654")  # Rei Branco ♔
    print("\u265F")  # Peão Preto ♟

    return input("Selecione o modo: ")



def verifica_cord(cord):
    if len(cord)!=2:
        raise ValueError('Coordenada inválida')
    letra, numero = cord[0].lower() , cord[1]
    if letra <'a' or letra > 'h':
        raise ValueError('Coluna inválida')
    if numero < '1' or numero > '8':
        raise ValueError('Linha inválida')

    return (ord(letra)-ord('a'), numero)



def jogador_1():
    origem = input("Jogador 1 (brancas) selecione uma peça ")
    origem = verifica_cord(origem)
    destino = input("Mova a peça ")
    destino = verifica_cord(destino)
    

def jogador_2():
    origem = input("Jogador 2 (pretas) selecione uma peça ")
    origem = verifica_cord(origem)
    destino = input("Mova a peça ")
    destino = verifica_cord(destino)




while state != 'finish':
    if state == 'start':
        modo = start()
        while modo != "2":
            print('Não disponível, selecione outro')
            modo = start()

        tabuleiro.show()

        jogador_1()
        jogador_2()
        state = 'finish'

    