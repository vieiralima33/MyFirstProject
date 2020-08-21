import PySimpleGUI as sg

class WindowScreen():
    def __init__(self):
        sg.change_look_and_feel('DarkGrey4')
        # Layout
        layout = [
            [sg.Text('\n Name', size=(11,0)), sg.Input(size=(18,0), key='name')],
            [sg.Text('\nWeight[Kg]', size=(11,0)), sg.Input(size=(18,0), key='weight')],
            [sg.Text('\nHeight[M]', size=(11,0)), sg.Input(size=(18,0), key='height')],
            [sg.Text('\n Gender')],
            [sg.Radio('Male', 'gender', size=(7,0), key='male'), sg.Radio('Female', 'gender', size=(7,0), key='female')],
            [sg.Button('Calculate')],
            [sg.Output(size=(32,8))]
        ]
        # Window
        self.window = sg.Window('Calculate Your BMI').layout(layout)

    def Start(self):
        while True:
            # Data Extract
            self.button, self.values = self.window.Read()
            name = str(self.values['name'])
            weight = int(self.values['weight'])
            height = float(self.values['height'])
            gmale = self.values['male']
            gfemale = self.values['female']
            imc = weight / height**2

            if gmale == True:
                print ('Your Body Mass Index is: ', round(imc,2))
                if imc < 20:
                    print('\nAttention', name, 'You are under weight for your height!')
                elif imc >= 20 and imc < 25:
                    print('\nCongratulations', name,  'your weight is normal for your height!')
                elif imc >= 25 and imc < 30:
                    print('\nAttention', name, 'you are overweight!')
                elif imc >= 30 and imc < 40:
                    print('\n Be careful', name, 'you have moderate obesity!')
                elif imc >= 43:
                    print('\n Seek help', name, 'you have morbid obesity!')

            if gfemale == True:
                print ('Your Body Mass Index is: ', round(imc,2))
                if imc < 19:
                    print('\nAttention', name, 'You are under weight for your height!')
                elif imc >= 19 and imc < 24:
                    print('\nCongratulations', name, 'your weight is normal for your height!')
                elif imc >= 24 and imc < 29:
                    print('\nAttention', name, 'you are overweight!')
                elif imc >= 29 and imc < 39:
                    print('\n Be careful', name, 'you have moderate obesity!')
                elif imc >= 39:
                    print('\n Seek help', name, 'you have morbid obesity!')

screen = WindowScreen()
screen.Start()