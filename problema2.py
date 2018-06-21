# -----------------------------------------------------------------------------------------
#
#       Solução Problema 2:
#
# Escreva um programa curto que imprima cada número de 1 a 100 em uma nova linha.
# Para cada múltiplo de 3, imprima "Hello" em vez do número.
# Para cada múltiplo de 7, imprima "World" em vez do número.
# Para números que são múltiplos de 3 e 7, imprima "HelloWorld" em vez do número.
#
# ------------------------------------------------------------------------------------------

for n in range(1, 101):
    if n % 3 == 0 and n % 7 == 0:
        print("Hello World")
    elif n % 3 == 0:
        print("Hello")
    elif n % 7 == 0:
        print("World")
    else:
        print('{} '. format(n))






