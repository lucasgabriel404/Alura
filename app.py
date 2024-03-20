import os

restaurantes = [{'nome':'Pizza','categoria':'Lanche','ativo':False},
                {'nome':'Hamburg','categoria':'Lanche','ativo':True},
                {'nome':'Churrasco','categoria':'Janta','ativo':False}]

def exibir_subtitulo(texto):
    ''' Essa função limpa o termina e exibe o título da opção selecionada no menu.
    Input:
    - texto: str - O texto do subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal():
    ''' Essa função solicita uma telca para voltar ao menu principal.
    Output:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal.\n')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é resposável por cadastrar um novo restaurante.
    Inputs:
    - Nome do Restaurante
    - Categoria do reastaurante

    Output:
    - Adiciona o novo restaurante na lista de restaurantes
    '''
    exibir_subtitulo('Cadastrar Novo Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}:\n')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    voltar_menu_principal()

def listar_restaurante_ativos():
    ''' Essa função lista somente os restaurantes ativos.
    Output:
    - Exibe os restaurantes ativos na tela
    '''
    exibir_subtitulo('Listagem de Restaurantes Ativos')
    print('Os restaurantes ativos são:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Desativado'
        if restaurante['ativo'] == True:
            print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}'  )
    voltar_menu_principal()

def listar_restaurantes():
    ''' Essa função lista todos os restaurantes cadastrados.
    Output:
    - Exibe os restaurantes na tela
    '''
    exibir_subtitulo('Listagem de Restaurantes')
    print('Os restaurantes cadastrados são:')
    print(f'{'Nome '.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)} ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}'  )
        
        
    #    print(restaurante.values())

    #x = 0
    #while x<len(restaurantes):
    #    print(restaurantes[x])
    #    x=x+1
    voltar_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função troca o status do restaurante entre ativo ou desativado.
    Output:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternar Estado do Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar:\n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu_principal()

def exibir_nome_do_programa():
    ''' Essa função exibe o nome estilizado do programa.'''
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ """)

def exibir_opcoes():
    ''' Essa função exibe as opções do aplicativo.'''
    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Aternar Status Restaurante')
    print ('4. Listar Restaurante Ativos')
    print ('5. Sair do Aplicativo \n')

def opcao_invalida():
    ''' Essa função exibe mensagem de erro e volta para o menu principal.
    Output:
    - Retorna ao menu principal
    '''
    print('Opção Inválida.\n')
    voltar_menu_principal()

def escolher_opcao():
    ''' Essa função seleciona a opção do menu principal.
    Output:
    - Executa a opção escolhida pelo usuário    
    '''
    try:
        opcao_escolhida = int(input ('Escolha uma opção:'))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            listar_restaurante_ativos()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()   

def finalizar_app():
    ''' Essa função finaliza o aplicativo.'''
    exibir_subtitulo('Encerrando app.')

def main():
    ''' Essa função inicializa o sistema.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()