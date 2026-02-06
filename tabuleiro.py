import numpy as np

# K: rei, Q: Dama, N:Cavalo, T: Torre, B: Bispo, p : peão 
# ⬜⬛ casas  

class ChessBoard:
    def __init__(self):
        self.chessboard = self._getboard((8,8))
            
    def _getboard(self, size : tuple):
        board = np.zeros(size)
        for i in range(size[0]):
            for j in range(size[1]):
                if (i + j) % 2 == 0:
                    board[i,j] = 1# 
                else:
                    board[i,j] = 0# 
        return board
    
    def show(self):
        mapping = {0 : "\U00002B1B",1 : "\U00002B1C"}
        i = 8
        for row in self.chessboard:
            print(i ,"".join(mapping[val] for val in row))
            i -= 1 
        print("  ", "a b c d e f g h")
    def get_coordinates(self, coordinate : tuple): # a4
        mapping = {"a":0, "b":1, "c":2, "d":3,
                   "e":4, "f":5, "g":6, "h":7}
        return self.chessboard[ mapping[coordinate[0]] ][ coordinate[1] - 1 ]

print("Hello World!")
tabuleiro = ChessBoard()
tabuleiro.show()
print(tabuleiro.get_coordinates(("a", 1)))