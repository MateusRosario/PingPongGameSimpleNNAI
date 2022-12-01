import os
class Event_Controler:
    def __init__(self, rede_p1, rede_p2):
        self.need_objects = True
        self.comandos = []
        self.redep1 = rede_p1
        self.redep2 = rede_p2

    def set_objects(self, bola, player_1, player_2, partida):
        self.bola = bola
        self.player_1 = player_1
        self.player_2 = player_2
        self.p1_controler = player_1.controle
        self.p2_controler = player_2.controle
        self.partida = partida

    def atualiza_lista(self):
        self.comandos = []
        a = self.bola.get_posicao()
        r1 = self.redep1.run([self.bola.get_posicao()[0], self.bola.get_posicao()[1], self.player_1.posicao.x])
        r2 = self.redep2.run([self.bola.get_posicao()[0], self.bola.get_posicao()[1], self.player_2.posicao.x])
        if r1 < 0.5:
            self.comandos.append(self.p1_controler.esquerda)
        else:
            self.comandos.append(self.p1_controler.direita)

        if r2 < 0.5:
            self.comandos.append(self.p2_controler.esquerda)
        else:
            self.comandos.append(self.p2_controler.direita)

    def get_eventos_list(self):
        self.atualiza_lista()
        return self.comandos

    def finalizar(self):
        self.salvar()

    def salvar(self):


        placar = self.partida.placar_p1 - self.partida.placar_p2
        salvar = self.redep1
        sufixo = '-P1'
        if placar < 0:
            salvar = self.redep2
            sufixo = '-P2'
            placar = -placar

        file = open('Redes' + sufixo + '.txt', 'a')

        file.write(str(placar) + ',')

        # Salva Pesos das Camadas Ocultas

        for a in range(len(salvar.hlw)):

            for b in range(len(salvar.hlw[a])):
                for c in range(len(salvar.hlw[a][b])):
                    if c is not len(salvar.hlw[a][b])-1:
                        file.write(str(salvar.hlw[a][b][c]) + ';')
                    else:
                        file.write(str(salvar.hlw[a][b][c]))
                if b is not len(salvar.hlw[a])-1:
                    file.write('_')

            if a is not len(salvar.hlw) - 1:
                file.write(':')

        #Salva Pesos da Camada de Saida
        file.write(',')
        for a in range(len(salvar.output_weights)):
            file.write('')
            for b in range(len(salvar.output_weights[a])):
                if b is not len(salvar.output_weights[a])-1:
                    file.write(str(salvar.output_weights[a][b]) + ';')
                else:
                    file.write(str(salvar.output_weights[a][b]))
            if a is not len(salvar.output_weights) - 1:
                file.write('_')

        # Salva os bias das Camadas ocultas
        file.write(',')
        for a in range(len(salvar.hlb)):
            file.write('')
            for b in range(len(salvar.hlb[a])):
                if b is not len(salvar.hlb[a]) - 1:
                    file.write(str(salvar.hlb[a][b]) + ';')
                else:
                    file.write(str(salvar.hlb[a][b]))
            if a is not len(salvar.hlb) - 1:
                file.write('_')

        # Salva os bias da Camada de Saida

        file.write(',')
        for a in range(len(salvar.output_bias)):
            if a is not len(salvar.output_bias) - 1:
                file.write(str(salvar.output_bias[a]) + ';')
            else:
                file.write(str(salvar.output_bias[a]))

        file.write('\n')
        file.close()
