import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkAmber')  # جایگزین sg.theme()

layout = [[sg.Text('سلام!')],
          [sg.Button('باشه')]]

window = sg.Window('پنجره آزمایشی', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'باشه':
        break
window.close()
