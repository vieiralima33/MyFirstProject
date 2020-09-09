import PySimpleGUI as sg

class Main():
    def __init__(self):
        sg.theme('Dark2')

        layout = [
            [sg.Text('\n Name', size=(11,0)), sg.InputText('', size=(18,0), key='name')],
            [sg.Text('\nWeight(Kg)', size=(11,0)), sg.Input('', size=(18,0), key='weight')],
            [sg.Text('\nHeight(cm)', size=(11,0)), sg.Input('', size=(18,0), key='height')],
            [sg.Radio('Male', 'gender', size=(7,0), key='male'), sg.Radio('Female', 'gender', size=(7,0), key='female')],
            [sg.Text('\n')],             
            [sg.Button('Calculate')],
            [sg.Output(size=(38,5))],
        ]

        self.window = sg.Window('Calculate Your BMI').layout(layout)

    def Start(self):
        while True:
            self.button, self.values = self.window.Read()
            name = str(self.values['name'])
            try:
                weight = int(self.values['weight'])
                height = int(self.values['height'])
            except ValueError:
                print('\nYou typed invalid characters, \nTry again with numbers for weight and height...')
                screen.Start()
            gmale = self.values['male']
            gfemale = self.values['female']
            imc = weight * 10000 / height**2
            print('\n' * 2)

            if gmale == True:
                print ('Your Body Mass Index is: ', round(imc,2))
                if imc < 20:
                    print('Attention', name, '\nYou are under weight for your height!')
                elif imc >= 20 and imc < 25:
                    print('Congratulations', name,  '\nYour weight is normal for your height!')
                elif imc >= 25 and imc < 30:
                    print('Attention', name, '\nYou are overweight!')
                elif imc >= 30 and imc < 40:
                    print('Be careful', name, '\nYou have moderate obesity!')
                elif imc >= 43:
                    print('Seek help', name, '\nYou have morbid obesity!')

            if gfemale == True:
                print ('Your Body Mass Index is: ', round(imc,2))
                if imc < 19:
                    print('Attention', name, '\nYou are under weight for your height!')
                elif imc >= 19 and imc < 24:
                    print('Congratulations', name, '\nYour weight is normal for your height!')
                elif imc >= 24 and imc < 29:
                    print('Attention', name, '\nYou are overweight!')
                elif imc >= 29 and imc < 39:
                    print('Be careful', name, '\nYou have moderate obesity!')
                elif imc >= 39:
                    print('Seek help', name, '\nYou have morbid obesity!')
            if gmale == False and gfemale == False:
                print ('Make sure you have selected your gender\n')
screen = Main()
screen.Start()