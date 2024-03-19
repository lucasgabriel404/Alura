def fase_da_vida():
    idade = int(input('Qual sua idade?'))

    if 0<=idade<=12:
        print(' É criança!')
    elif 13<=idade<=18:
        print(' É adolescente!')
    elif idade>18:
        print(' É adulto!')
    else:
        print('Idade inválida.')

fase_da_vida()