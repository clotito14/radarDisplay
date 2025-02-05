import urllib.request
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence

# retrieve KLOT loop gif from internet
urllib.request.urlretrieve('https://radar.weather.gov/ridge/standard/KLOT_loop.gif', 'KLOT_loop.gif')
klot_loop_gif_path = 'KLOT_loop.gif'
gif_filename = klot_loop_gif_path

layout = [[sg.Image(key='-IMAGE-')]]

window = sg.Window('KLOT Standard', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

interframe_duration = Image.open(gif_filename).info['duration']

while True:
    for frame in ImageSequence.Iterator(Image.open(gif_filename)):
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit(0)
        window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )