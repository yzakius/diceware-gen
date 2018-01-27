import random

counter = 1

while counter == 1:

    faces = int(input('Quantos lados tem o dado? '))
    blocks = int(input('Quantas blocos tem a senha?  '))
    
    print('Rolando dados...')
    print("{} lados com {} blocos".format(faces, blocks))
    print('-' * 39)

    x = 0
    lista = []
    y = 0
    incremento = 0


    while x < blocks * 5: # cada bloco vai rolar o dado 5x.
        x += 1            # contador
        result = random.randint(1, faces)
        lista.append(result)

    s = ''
    for i in lista:
        s = s + str(i)
    lista = [s]
    result = ''.join(lista)

    print('Resultado total: {}'.format(result))
    print('-' * 39)
    print('Resultado por blocos:')

    while y < blocks:
        y += 1
        print('Bloco {}: {} '.format(y, result[incremento:incremento + 5]))
        incremento = incremento + 5
        
    choice = str(input('Deseja rolar mais dados? [S/N]'))
    if choice == 'S' or choice == 's':
        counter = 1
    else:
        counter = 0
