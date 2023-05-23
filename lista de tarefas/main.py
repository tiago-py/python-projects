import PySimpleGUI as sg 
import sqlite3


conn = sqlite3.connect('listaTarefas.db')
cursor = conn.cursor()
tarefas = []
def janela():
    tarefa = 'Tarefa'
    sg.theme('DarkBlue')
    layout = [
        [sg.Text(f'{tarefa:<11}'), sg.Input(key='Tarefa', size=(20, 1))],
        [sg.Button('Cadastrar Nova Tarefa')],
        [sg.Listbox('Tarefa',size=(50,10), key='-BOX-')],
        [sg.Button('Deletar'), sg.Button('Sair')]
    ]
    return sg.Window('lista de tarefas',layout=layout,finalize=True)

janela1 = janela()
id_tarefa = 1
while True:
    window, event, values = sg.read_all_windows()
    button, values = window.read()
    if window == janela1 and event == sg.WIN_CLOSED or button == "Sair":
        break
    elif button == "Cadastrar Nova Tarefa":
        dados = values['Tarefa'].capitalize()
        cursor.execute("INSERT INTO task(task) VALUES(?)", [dados])
        tarefas.append(values['Tarefa'.capitalize()])
        conn.commit()
        print("Adicionado com sucesso ao banco")
    elif button == "Deletar":
        cursor.execute('''
                DELETE FROM task
                WHERE id = ?
        ''', [id_tarefa])
        conn.commit()
        print("Deletado com sucesso do banco")