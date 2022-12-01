import random
import numpy as np

class Rede:
    def __init__(self, num_entradas, num_camadas_ocultas, num_nos_p_camada, num_saidas, pesos_aleatorios=True, diretorio=None, pos_dados_file=None):
        self.num_in = num_entradas
        self.num_l = num_camadas_ocultas
        self.num_n = num_nos_p_camada
        self.num_out = num_saidas
        if pesos_aleatorios:
            self.hlb = [[0 for a in range(num_nos_p_camada)] for a in
                        range(num_camadas_ocultas)]  # hlb = hidden_layers_bias = vieses das camadas ocultas
            self.output_bias = [0 for a in range(num_saidas)]
            self.set_weights_random(-1, 1, 3)
        else:
            self.set_weights_file(diretorio, pos_dados_file)

    def run(self, entradas):
        results = entradas
        for l in range(len(self.hlw)):
            results = np.dot(results, np.transpose(self.hlw[l]))
            results = results + self.hlb[l]
            results = self.ReLU(results)
        saida = np.dot(results, np.transpose(self.output_weights))
        saida = saida + self.output_bias
        saida = self.sigmoide(saida)
        return saida

    def sigmoide(self, saidas):
        return 1/(1+np.power(np.e, np.multiply(-1, saidas)))

    def ReLU(self, saidas):
        return np.maximum(0, saidas)

    def set_weights_random(self, lim_inf=-1, lim_sup=1, precisao=3):
        precisao = np.power(10, precisao)
        lim_inf = lim_inf * precisao
        lim_sup = lim_sup * precisao

        self.hlw = [[[] for a in range(self.num_n)] for a in
                    range(self.num_l)]  # hlw = hidden_layers_weights = pesos das camadas ocultas
        for i in range(0, len(self.hlw)):
            if i is 0:
                for a in self.hlw[i]:
                    for n in range(self.num_in):
                        a.append(random.randint(lim_inf, lim_sup) / precisao)
            else:
                for a in self.hlw[i]:
                    for n in range(self.num_n):
                        a.append(random.randint(lim_inf, lim_sup) / precisao)

        self.output_weights = [[random.randint(lim_inf, lim_sup) / precisao for a in range(self.num_n)] for a in
                               range(self.num_out)]

    def set_weights_file(self, diretorio, pos):
        file = open(diretorio, 'r')
        for i in range(pos-1):
            file.readline()
        dados = file.readline().split(',')
        self.hlw = dados[1].split(':')
        for i in range(len(self.hlw)):
            self.hlw[i] = self.hlw[i].split('_')
            for b in range(len(self.hlw[i])):
                self.hlw[i][b] = self.hlw[i][b].split(';')
        for a in range(len(self.hlw)):
            for b in range(len(self.hlw[a])):
                for c in range(len(self.hlw[a][b])):
                    self.hlw[a][b][c] = float(self.hlw[a][b][c])

        self.output_weights = dados[2].split('_')
        for a in range(len(self.output_weights)):
            self.output_weights[a] = self.output_weights[a].split(';')
        for a in range(len(self.output_weights)):
            for b in range(len(self.output_weights[a])):
                self.output_weights[a][b] = float(self.output_weights[a][b])

        self.hlb = dados[3].split('_')
        for a in range(len(self.hlb)):
            self.hlb[a] = self.hlb[a].split(';')
        for a in range(len(self.hlb)):
            for b in range(len(self.hlb[a])):
                self.hlb[a][b] = float(self.hlb[a][b])

        self.output_bias = dados[4].split(';')
        for a in range(len(self.output_bias)):
            self.output_bias[a] = float(self.output_bias[a])

        file.close()


if __name__ == '__main__':
    A = Rede(3, 3, 5, 1)
    print(A.run([1, 1, 1]))
