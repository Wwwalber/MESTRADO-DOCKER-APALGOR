from collections import deque


grafo = {}
grafo["você"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []
# A ordem que adicionamos os pares chave/valor no dicionário não importa, pois os dicionários em Python não mantêm a ordem de inserção dos elementos.

# anujm, peggy, thom e hohnny não possuem conexões com ninguém, então seus valores são listas vazias.

# grafos direcionados são conhecidos como digrafos.

def busca_vendedor_de_manga():
    fila_de_pesquisa = deque() 
    fila_de_pesquisa += grafo["você"] # adiciona todos os amigos da lista de amigos de você na fila de pesquisa
    while fila_de_pesquisa: # enquanto a fila de pesquisa não estiver vazia
        pessoa = fila_de_pesquisa.popleft() # pega a primeira pessoa da fila
        if pessoa_e_vendedor(pessoa): # verifica se a pessoa é um vendedor de manga
            print(pessoa + " é um vendedor de manga!")
            return True
        else:
            fila_de_pesquisa += grafo[pessoa] # adiciona os amigos da pessoa na fila de pesquisa
    return False

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm' # retorna True se o último caractere do nome for 'm'
