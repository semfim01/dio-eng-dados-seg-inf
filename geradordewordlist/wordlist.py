import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))
# ele pega  caracter e monta aleatoriamente 

for i in resultado:
    print(''.join(i))


