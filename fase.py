# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO


VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []
        # self._passaros_lancados = []

    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase

        :param obstaculos: Tupla de objetos obstáculos
        """
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase

        :param porcos: Tupla de objetos porcos
        """
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase

        :param passaros: Tupla de objetos passaros
        """
        self._passaros.extend(passaros)

    def _todos_porcos_destruidos(self):
        """
        Informa se todos os porcos foram destruídos.
        :return: Bool
        """
        return all(map(lambda ator: ator.status == 'Destruido', self._porcos))

    def _todos_passaros_destruidos(self):
        """
        Informa se todos os pássaros foram destruídos.
        :return: Bool
        """
        return all(map(lambda ator: ator.status == 'Destruido', self._passaros))

    def status(self):
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return: Constante que indica o status do jogo
        """
        if self._todos_porcos_destruidos():
            return VITORIA
        if self._todos_passaros_destruidos():
            return DERROTA

        return EM_ANDAMENTO

    def _passaros_a_lancar(self):
        """
        :return: Lista de passaros que não foram lançados.
        """
        '''
        A linha abaixo itera em self._passaros coletando os valores onde ator.foi_lancado é falso.
        Transforma os valores coletados em uma lista.
        '''
        return list(filter(lambda ator: ator.foi_lancado() is False, self._passaros))

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """

        passaros_disponiveis = self._passaros_a_lancar()
        if passaros_disponiveis:
            passaros_disponiveis[0].lancar(angulo, tempo)



    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.

        Cada ator deve ser transformado em um Ponto.

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        for passaro in self._passaros:
            passaro.calcular_posicao(tempo)
            for alvo in self._obstaculos + self._porcos:
                passaro.colidir(alvo, self.intervalo_de_colisao)
                passaro.colidir_com_chao()
        pontos=[self._transformar_em_ponto(a) for a in self._passaros+self._obstaculos+self._porcos]

        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())

