from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

klot_loop_gif_path = 'https://radar.weather.gov/ridge/standard/KLOT_loop.gif'

img = np.asarray(Image.open(klot_loop_gif_path)) 

imgplot = plt.imshow(img)