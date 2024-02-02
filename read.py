# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("Last message before you host! This is the original project to host local websites. Made by SergeiTregub.")], [sg.Button("Host")]]

# Create the window
window = sg.Window("v1.2", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Host" or event == sg.WIN_CLOSED:
        break

window.close()