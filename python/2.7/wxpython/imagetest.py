#!/usr/local/bin/python2.7

import sys
import os

# Display using WXPython
import matplotlib
matplotlib.use('WXAgg')

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# Unbuffer prints
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stdout = unbuffered

# --- #
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

print "The container is working properly if a plot shows a sigmoid function."

print "WXAgg is used as the rendering backend."

x = np.arange(-8, 8, 0.1);
plt.plot(x, sigmoid(x), label="sigmoid(x)")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("sigmoid")
plt.show()
plt.savefig("sigmoid.png")
