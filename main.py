import PySimpleGUI as sg

sg.theme('Dark2')
def main():
    layout = [
        [sg.Text('Welcome')],
        [sg.Text('Choose your language')],
        [sg.Button('English'), sg.Button('Portuguese')]
        ]
    window = sg.Window('Welcome', layout, size=(440,140), element_justification='center')
    button, values = window.read()
    if button == 'Portuguese':
        window.close()
        import portuguese
    if button == 'English':
        window.close()
        import english
main()