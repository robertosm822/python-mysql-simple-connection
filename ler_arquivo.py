# -*- coding: utf-8 -*-
# w => escreve 1 vez , a => escreve linha a linha
w = open("texto.txt", "a+")

w.write("linha 3\n")
w.close()