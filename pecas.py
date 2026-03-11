from abc import ABC, abstractmethod
class Peca(ABC):
    simbolos = {
        ("rei","branco"):"♔",
        ("rainha","branco"):"♕",
        ("torre","branco"):"♖",
        ("bispo","branco"):"♗",
        ("cavalo","branco"):"♘",
        ("peao","branco"):"♙",

        ("rei","preto"):"♚",
        ("rainha","preto"):"♛",
        ("torre","preto"):"♜",
        ("bispo","preto"):"♝",
        ("cavalo","preto"):"♞",
        ("peao","preto"):"♟",
    }
        
    def __init__(self, cor):
        self.cor = cor

    def simbolo(self):
        return self.simbolos[(self.tipo, self.cor)]
    
    @abstractmethod
    def movimentos_validos(self, posicao, tabuleiro):
        pass

class Torre(Peca):

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        linha, coluna = posicao

        direcoes = [(1,0), (-1,0), (0,1), (0,-1)]

        for dl, dc in direcoes:
            l, c = linha + dl, coluna + dc

            while tabuleiro.dentro(l, c):
                peca = tabuleiro.get(l, c)

                if peca is None:
                    movimentos.append((l, c))
                else:
                    if peca.cor != self.cor:
                        movimentos.append((l, c))
                    break

                l += dl
                c += dc

        return movimentos
    
