import pygame
from Player import Player
from Campo import Campo
from Estremidade import Estremidade
from Point import Point
from Controle_player import Controle_player
from partida import partida
from Neural_Net.Event_Controler import Event_Controler
from Neural_Net.Rede import Rede


def runWithIAs():
    size = Largura, Altura = 500, 600

    pygame.init()
    pygame.font.init()

    for i in range(1):
        bottom = Estremidade(Point(10, Altura - 10), Point(Largura - 10, Altura - 10), "marca_ponto")
        top = Estremidade(Point(10, 10), Point(Largura - 10, 10), "marca_ponto")
        left = Estremidade(Point(10, 10), Point(10, Altura - 10), "reflete")
        right = Estremidade(Point(Largura - 10, 10), Point(Largura - 10, Altura - 10), "reflete")


        eventos = Event_Controler(Rede(3, 2, 3, 1, pos_dados_file=64, diretorio='Redes-P1.txt', pesos_aleatorios=False), Rede(3, 2, 3, 1, pos_dados_file=23, diretorio='Redes-P2.txt', pesos_aleatorios=False))

        p1 = Player(1, [255, 0, 0], 1, 2, 3, bottom, Controle_player('right', 'left'))
        p2 = Player(2, [255, 0, 0], 1, 2, 3, top, Controle_player('dir', 'esq'))

        a = partida(pygame.display.set_mode(size), p1, p2, Campo(left, right, top, bottom), eventos, 100, placar_max=100)

def thanos(diretorio, fit):
    file = open(diretorio, 'r')
    text = []
    text.append(file.readline())
    while text[len(text)-1] == '':
        text.append(file.readline())
    file.close()

    text.remove('')

    new_file = open(diretorio, 'w')
    for i in text:
        if int(i.split(',')[0]) > fit:
            new_file.write(i)
    new_file.close()


if __name__ == '__main__':
    runWithIAs()
