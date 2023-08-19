import PySimpleGUI as sg
import datetime

sg.theme('Reddit')

layout = [
    [sg.Text('Contagem Regressiva Para Te Ver', font=('Helvetica', 20))],
    [sg.Text('', size=(30, 2), key='countdown')],
    [sg.Button('Sair')]
]

window = sg.Window('Contagem Regressiva', layout, finalize=True)

target_date = datetime.datetime(2023, 9, 7)

while True:
    event, values = window.read(timeout=1000)

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    current_date = datetime.datetime.now()
    time_left = target_date - current_date

    if time_left.total_seconds() <= 0:
        window['countdown'].update("A data alvo já foi alcançada!")
    else:
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_text = f"Faltam {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos"
        window['countdown'].update(countdown_text)

window.close()
