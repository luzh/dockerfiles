#!/usr/local/bin/python2.7

import sys
import os

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# Change the TkAgg cursor type
from matplotlib.backend_bases import cursors
import matplotlib.backends.backend_tkagg as tkagg
tkagg.cursord[cursors.POINTER] = 'left_ptr'

# Unbuffer prints
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stdout = unbuffered

# --- #
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

print "The container is working properly if a plot shows a sigmoid function."

print "TkAgg is used as the rendering backend."

x = np.arange(-8, 8, 0.1);
fig = plt.figure()
plt.plot(x, sigmoid(x), label="sigmoid(x)")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("sigmoid")
plt.show()
fig.savefig("sigmoid.png")

img = Image.open("sigmoid.png")
(img_x_size, img_y_size) = img.size
img.close()

print "Pillow showing the plot has resolution", img_x_size, "x", img_y_size
