class Direcao:

    direcoes_possiveis = ('Norte', 'Leste', 'Sul', 'Oeste')

    def __init__(self):
        self.__direcao = 0

    def girar_a_direita(self):
        self.__direcao = (self.__direcao + 1) % len(Direcao.direcoes_possiveis)

    def girar_a_esquerda(self):
        self.__direcao = (self.__direcao - 1) % len(Direcao.direcoes_possiveis)

    def get_direcao(self):
        return self.direcoes_possiveis[self.__direcao]


if __name__ == "__main__":
    # Testando Direcao
    direcao = Direcao()
    print(direcao.get_direcao())
    direcao.girar_a_direita()
    print(direcao.get_direcao())
    direcao.girar_a_direita()
    print(direcao.get_direcao())
    direcao.girar_a_direita()
    print(direcao.get_direcao())
    direcao.girar_a_direita()
    print(direcao.get_direcao())
    direcao.girar_a_esquerda()
    print(direcao.get_direcao())
    direcao.girar_a_esquerda()
    print(direcao.get_direcao())
    direcao.girar_a_esquerda()
    print(direcao.get_direcao())
    direcao.girar_a_esquerda()
    print(direcao.get_direcao())