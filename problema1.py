# ---------------------------------------------------------------------------------------------------------------------
#
#       Solução Problema 1:
#
# Observe que sua base e altura tem comprimentos iguais e a imagem é desenhada usando somente o símbolo # e espaços.
# A última linha (base) não é precedida por nenhum espaço.
# Escreva um programa que imprima uma escada de tamanho n .
# Formato de entrada:
# Um único inteiro, denotando o tamanho da escada.
# Formato de saída:
# Imprima uma escada de tamanho n usando # símbolos e espaços.
#
# ---------------------------------------------------------------------------------------------------------------------


numero_linhas = int(input("Digite o número da entrada: "))
altura = numero_linhas
i = 1
while numero_linhas > 0:
    for i in range(numero_linhas):
        print(" ")
        i = i + 1
    while i <= altura:
        print("#".format())
        i = i + 1
    numero_linhas = numero_linhas - 1
