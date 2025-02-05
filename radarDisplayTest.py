import urllib.request
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence
import keyboard

# retrieve KLOT loop gif from internet
urllib.request.urlretrieve('https://radar.weather.gov/ridge/standard/KLOT_loop.gif', 'KLOT_loop.gif')
klot_loop_gif_path = 'KLOT_loop.gif'
gif_filename = klot_loop_gif_path   # by default

urllib.request.urlretrieve('https://radar.weather.gov/ridge/standard/base_velocity/KLOT_loop.gif', 'KLOT_loop_velo.gif')
klot_loop_velo_gif_path = 'KLOT_loop_velo.gif'

# keypress detection logic
def on_key_event(event):
    # get keypress
    key = event.name
    global gif_filename

    # Perform your control actions here
    if key == 'Q':
        keyboard.unhook_all()
        exit()
    elif key == '1':
        gif_filename = 'KLOT_loop.gif'
    elif key == '2':
        gif_filename = 'KLOT_loop_velo.gif'
    else:
        return

# listen to keypresses
keyboard.on_press(on_key_event)

layout = [[sg.Image(key='-IMAGE-')]]

window = sg.Window('KLOT Standard', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

interframe_duration = Image.open(gif_filename).info['duration']

while True:
    for frame in ImageSequence.Iterator(Image.open(gif_filename)):
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit(0)
        window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )