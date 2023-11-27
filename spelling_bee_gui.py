
# *** WIP ***


import PySimpleGUI as sg

def openWindow():
    sg.theme('LightYellow')
    layout = [
        [sg.Text('Enter the key letter that every word must contain: '), sg.InputText(key='input')],
        [sg.Text('Enter 6 other letters that words may or may not contain: '), sg.InputText(key='input')],
        [sg.Button("OK", key='OK'), sg.Button("Cancel")]
    ]

    window = sg.Window("Pokevent Tool", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

    window.close()

    results = scrape()

def scrape():
    print("p")

def main():
    openWindow()
main()
