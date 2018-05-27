import math

class JogoDaVelha(object):

    @staticmethod
    def estado_inicial():
        res = [0 for i in range(9)]
        return res

    @staticmethod
    def acoes(estado_atual,jogador):
        acoes = []
        for i in range(len(estado_atual)):
            if estado_atual[i] == 0:
                nova_acao = [i for i in estado_atual]
                nova_acao[i] = jogador
                acoes.append(nova_acao)
        return acoes
    @staticmethod
    def estado_terminal(estado_atual):
        if estado_atual[0] != 0 and estado_atual[0] == estado_atual[1] and estado_atual[1] == estado_atual[2]:
            return True, estado_atual[0]
        if estado_atual[3] != 0 and estado_atual[3] == estado_atual[4] and estado_atual[4] == estado_atual[5]:
            return True, estado_atual[3]
        if estado_atual[6] != 0 and estado_atual[6] == estado_atual[7] and estado_atual[7] == estado_atual[8]:
            return True, estado_atual[6]
        if estado_atual[0] != 0 and estado_atual[0] == estado_atual[4] and estado_atual[4] == estado_atual[8]:
            return True, estado_atual[0]
        if estado_atual[2] != 0 and estado_atual[2] == estado_atual[4] and estado_atual[4] == estado_atual[6]:
            return True, estado_atual[2]
        if estado_atual[0] != 0 and estado_atual[0] == estado_atual[3] and estado_atual[3] == estado_atual[6]:
            return True, estado_atual[0]
        if estado_atual[1] != 0 and estado_atual[1] == estado_atual[4] and estado_atual[4] == estado_atual[7]:
            return True, estado_atual[1]
        if estado_atual[2] != 0 and estado_atual[2] == estado_atual[5] and estado_atual[5] == estado_atual[8]:
            return True, estado_atual[2]
        if 0 in estado_atual:
            return False, 0
        else:
            return True, 0


def maior(x, y):
    if x > y:
        return x, 0
    else:
        return y, 1


def menor(x, y):
    if x < y:
        return x,0
    else:
        return y,1


def minimax(estado,jogador):
    v = math.inf
    acao = []
    for a in JogoDaVelha.acoes(estado,jogador):
        t = maior(v, valor_min(a, jogador))
        v = t[0]
        if t[1] == 1:
            acao = a
    return acao


def valor_max(estado,jogador):
    t = JogoDaVelha.estado_terminal(estado)
    if t[0]:
        return t[1]
    v = -math.inf
    acoes = JogoDaVelha.acoes(estado, jogador)
    #print(acoes)
    for a in acoes:
        v = maior(v,valor_min(a,-jogador))[0]
    return v


def valor_min(estado,jogador):
    t = JogoDaVelha.estado_terminal(estado)
    if t[0]:
        return t[1]
    v = math.inf
    acoes = JogoDaVelha.acoes(estado, jogador)
    #print(acoes)
    for a in acoes:
        v = menor(v, valor_max(a, -jogador))[0]
    return v


print(valor_max(JogoDaVelha.estado_inicial(), 1))