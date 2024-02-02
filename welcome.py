import PySimpleGUI as sg

layout = [[sg.Text("Welcome to DragonHost")], [sg.Button("Continue")]]

# Create the window
window = sg.Window("v1.2", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Continue" or event == sg.WIN_CLOSED:
        break

window.close()