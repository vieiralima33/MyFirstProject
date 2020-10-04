import PySimpleGUI as sg

sg.theme('Dark2')
class Indice():
    def __init__(self):
        layout = [
            [sg.Text('\n Nome', size=(11,0)), sg.InputText('', size=(22,0), key='nome')],
            [sg.Text('\nPeso(Kg)', size=(11,0)), sg.Input('', size=(22,0), key='peso')],
            [sg.Text('\nAltura(cm)', size=(11,0)), sg.Input('', size=(22,0), key='altura')],
            [sg.Radio('Masculino', 'genero', size=(7,0), key='masculino'), sg.Radio('Feminino', 'genero', size=(7,0), key='feminino')],
            [sg.Text('\n')],             
            [sg.Button('Calcular'), sg.Button('Sair')],
            [sg.Output(size=(38,5))],
        ]

        self.window = sg.Window('Calcule Seu IMC').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.window.Read()
            nome = str(self.values['nome'])
            if self.button == 'Sair':
                self.window.close()  
            try:
                peso = int(self.values['peso'])
                altura = int(self.values['altura'])
            except ValueError:
                print('\nVocê digitou carácteres inválidos, \nTente novamente com números para seu peso e altura...')
                screen.Iniciar()
            gmasculino = self.values['masculino']
            gfeminino = self.values['feminino']
            imc = peso * 10000 / altura**2
            print('\n' * 2)

            if gmasculino == True:
                print ('Seu Índice de Massa Corporal é: ', round(imc,2))
                if imc < 20:
                    print('Atenção', nome, '\nVocê está abaixo do peso!')
                elif imc >= 20 and imc < 25:
                    print('Parabéns', nome,  '\nSeu peso está normal!')
                elif imc >= 25 and imc < 30:
                    print('Atenção', nome, '\nVocê está acima do peso!')
                elif imc >= 30 and imc < 40:
                    print('Cuidado', nome, '\nVocê tem obesidade moderada!')
                elif imc >= 43:
                    print('Procure ajuda', nome, '\nVocê tem obesidade mórbida!')

            if gfeminino == True:
                print ('Seu Índice de Massa Corporal é: ', round(imc,2))
                if imc < 19:
                    print('Atenção', nome, '\nVocê está abaixo do peso!')
                elif imc >= 19 and imc < 24:
                    print('Parabéns', nome, '\nSeu peso está normal!')
                elif imc >= 24 and imc < 29:
                    print('Atenção', nome, '\nVocê está acima do peso!')
                elif imc >= 29 and imc < 39:
                    print('Cuidado', nome, '\nVocê tem obesidade moderada!')
                elif imc >= 39:
                    print('Procure ajuda', nome, '\nVocê tem obesidade mórbida!')
            if gmasculino == False and gfeminino == False:
                print ('Certifique-se de selecionar seu gênero\n')
screen = Indice()
screen.Iniciar()