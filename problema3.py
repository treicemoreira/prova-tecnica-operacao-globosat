# --------------------------------------------------------------------------------------------------------------
#
#       Solução Problema 3:
#
# Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas diagonais.
# Cada linha contém números inteiros separados por espaços descrevendo os itens da matriz.
#
# ---------------------------------------------------------------------------------------------------------------

matriz = []
soma = 0
n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))


def construirMatriz(m, n, matriz, soma):
    for i in range(1, n + 1):
        linha = []
        for j in range(1, m + 1):
            x = int(input("Digite o elemento %i%i da matriz: " % (i, j)))
            linha.append(x)
        matriz.append(linha)

    for i in range(n):
        for j in  range(m):
            for i in range(n):
               if linha[i] == linha[j]:
                 somaPrincipal = int (soma + linha[i][j])
              elif linha[i][j] == linha[j][i]:
                 somaSecundaria = int (somaSecundaria + linha[i][j])


DiferencaSomas = int (somaPrincipal - somaSecundaria)

construirMatriz(m, n, matriz, DiferencaSomas)

