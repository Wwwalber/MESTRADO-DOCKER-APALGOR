import random

'''
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.

O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os números deles, de 1 até N, são atribuídos de acordo com a ordem alfabética, mas os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.

Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do aluno que deve receber o bônus.

Entrada
A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 ≤ K ≤ N ≤ 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.
'''
def quicksortRecursivo(array, esq, dir):
    i = esq
    j = dir
    pivo = array[(dir + esq) // 2]

    while i <= j:
        while array[i] < pivo:
            i += 1
        while array[j] > pivo:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if esq < j:
        quicksortRecursivo(array, esq, j)
    if i < dir:
        quicksortRecursivo(array, i, dir)

def quicksort(array):
    quicksortRecursivo(array, 0, len(array) - 1)

# Leitura dos valores de N e K
N, K = map(int, input().split())

# Leitura dos nomes dos alunos
nomes = [input().strip() for _ in range(N)]

# Ordenação dos nomes em ordem alfabética
quicksort(nomes)

# Determinação do K-ésimo aluno na lista ordenada
print(nomes[K-1])



