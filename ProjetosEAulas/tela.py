import PySimpleGUI as sg # Chama o PySimpleGUI

class TelaPython: # Cria uma classe
    def __init__(self): # Cria uma função
        sg.change_look_and_feel('DarkPurple4') # Define qual cor será seu projeto
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')], # Cria um campo para inserir o nome
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')], # Cria um campo para inserir a idade
            [sg.Text('Quais provedores de e-mail são aceitos?')], # Cria uma pergunta
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')], # Cria um campo de check para selecionar 1 ou 3 emails
            [sg.Text('Aceita cartão')], # Cria uma pergunta
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')], # Cria um campo para selecionar uma unica opção
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')], # Cria um campo para velocidade do script ???
            [sg.Button('Enviar Dados')], # Cria um botão para enviar
            [sg.Output(size=(30,20))] # Cria um campo de saida de dados
        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout) # Cria um nome para a sua janela

    def Iniciar(self):
        while True:
            # Extrair os dados da Tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartao: {aceita_cartao}')
            print(f'Não Aceita Cartao: {nao_aceita_cartao}')
            print(f'Velocidade Script: {velocidade_script}')
tela = TelaPython()
tela.Iniciar()