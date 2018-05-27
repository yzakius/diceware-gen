from random import randint

def rolar_dados(quantidade_rolagem):
    for i in range(1, quantidade_rolagem + 1):
        print(randint(1, quantidade_rolagem), end='')
    print()

def blocos(quantidade_blocos, quantidade_rolagem):
    x = 0
    while x < quantidade_blocos:
        rolar_dados(quantidade_rolagem)
        x += 1

quantidade_blocos = int(input('Quantidade de Blocos da Senha: '))
quantidade_rolagem = int(input('Quantidade de Rolagens do Dado: '))
print('Rolando dados...')
print('Resultado')
print('*' * 10)
blocos(quantidade_blocos, quantidade_rolagem)
