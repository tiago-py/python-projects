import PySimpleGUI as sg
from random import randint
import dbase
from dbase import mostrarDados
def janela_cadastro():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Text('Email')],
        [sg.Input()],
        [sg.Text('Senha')],
        [sg.Input()],
        [sg.Button('Cadastrar')],
    ]
    return sg.Window('Login',layout=layout,finalize=True)
def janela_login():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Nome')],
        [sg.Input(key='Nome')],
        [sg.Text('Senha')],
        [sg.Input(key='Senha')],
        [sg.Button('Login')],
    ]
    return sg.Window('Login',layout=layout,finalize=True)

def janela_add():
    n = 'Nome'
    e = 'Email'
    nas = 'Senha'
    sg.theme('DarkBlue')
    layout2 = [
        [sg.Text(f'{n:<11}'), sg.Input(key='nome', size=(20, 1))],
        [sg.Text(f'{e:<12}'), sg.Input(key='email', size=(20, 1))],
        [sg.Text(f'{nas:<4}'), sg.Input(key='senha', size=(20, 1))],
        [sg.Button('Cadastrar Novo Usuário')],
        [sg.Listbox('Nome', 'Email', 'Senha', size=(50,10), key='-BOX-'), mostrarDados()],
        [sg.Button('Deletar'), sg.Button('Sair')]

    ]
    return sg.Window('cadastro pessoas',layout=layout2,finalize=True)

janela1, janela2, janela3 = janela_add(), None, None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event ==  sg.WIN_CLOSED:
        break
    elif window == janela1 and event == 'Cadastrar':
        janela2 = janela_login()
        janela1.hide()
    elif window == janela2 and event ==  sg.WIN_CLOSED:
        break
    
    elif window == janela2 and event == 'Login':
        janela3 = janela_add()
        janela2.hide()
    elif window == janela3 and event ==  sg.WIN_CLOSED:
        break
    while True:
        button, values = window.read()
        if button == 'Cadastrar Novo Usuário':
            id = randint(1, 999)
            nome = values['nome'].capitalize()
            email = values['email'].capitalize()
            senha = values['senha'].capitalize()
        if nome != '':
            dbase.write(id, nome, email, senha)
        window.find_element('nome').Update('')
        if button == 'Deletar':
            if nome:        
                x = values['-BOX-'][0]
                dbase.delete(x)