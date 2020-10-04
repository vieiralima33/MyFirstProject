import PySimpleGUI as sg

sg.theme('Dark2')
class Main():
    def __init__(self):
        layout = [
            [sg.Text('\n Name', size=(11,0)), sg.InputText('', size=(22,0), key='name')],
            [sg.Text('\nWeight(Kg)', size=(11,0)), sg.Input('', size=(22,0), key='weight')],
            [sg.Text('\nHeight(cm)', size=(11,0)), sg.Input('', size=(22,0), key='height')],
            [sg.Radio('Male', 'gender', size=(7,0), key='male'), sg.Radio('Female', 'gender', size=(7,0), key='female')],
            [sg.Text('\n')],             
            [sg.Button('Calculate'), sg.Button('Exit')],
            [sg.Output(size=(38,5))],
        ]

        self.window = sg.Window('Calculate Your BMI').layout(layout)

    def Start(self):
        while True:
            self.button, self.values = self.window.Read()
            name = str(self.values['name'])
            if self.button == 'Exit':
                self.window.close()  
            try:
                weight = int(self.values['weight'])
                height = int(self.values['height'])
            except ValueError:
                print('\nYou typed invalid characters, \nTry again with numbers for weight and height...')
                screen.Start()
            gmale = self.values['male']
            gfemale = self.values['female']
            bmi = weight * 10000 / height**2
            print('\n' * 2)

            if gmale == True:
                print ('Your Body Mass Index is: ', round(bmi,2))
                if bmi < 20:
                    print('Attention', name, '\nYou are under weight for your height!')
                elif bmi >= 20 and bmi < 25:
                    print('Congratulations', name,  '\nYour weight is normal for your height!')
                elif bmi >= 25 and bmi < 30:
                    print('Attention', name, '\nYou are overweight!')
                elif bmi >= 30 and bmi < 40:
                    print('Be careful', name, '\nYou have moderate obesity!')
                elif bmi >= 43:
                    print('Seek help', name, '\nYou have morbid obesity!')

            if gfemale == True:
                print ('Your Body Mass Index is: ', round(bmi,2))
                if bmi < 19:
                    print('Attention', name, '\nYou are under weight for your height!')
                elif bmi >= 19 and bmi < 24:
                    print('Congratulations', name, '\nYour weight is normal for your height!')
                elif bmi >= 24 and bmi < 29:
                    print('Attention', name, '\nYou are overweight!')
                elif bmi >= 29 and bmi < 39:
                    print('Be careful', name, '\nYou have moderate obesity!')
                elif bmi >= 39:
                    print('Seek help', name, '\nYou have morbid obesity!')
            if gmale == False and gfemale == False:
                print ('Make sure you have selected your gender\n')
screen = Main()
screen.Start()