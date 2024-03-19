import os

def localizacao_plano_cartesiano(x,y):
    if x>0 and y>0:
        print('Primeiro Quadrante!')
    elif x<0 and y>0:
        print('Segundo Quadrante!')
    elif x<0 and y<0:
        print('Terceiro Quadrante!')
    elif x>0 and y<0:
        print('Quarto Quadrante!')
    else:
        print('O ponto está no eixo ou origem!')

def main():
    os.system('cls')
    x = int(input('Digite a coordenada X:\n'))
    y = int(input('Digite a coordenada Y:\n'))
    localizacao_plano_cartesiano(x,y)

if __name__ == '__main__':
    main()