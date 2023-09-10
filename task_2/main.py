import board
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

data = np.random.randint(2, size=(50, 50))

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='Greens', animated=True)

def update(i):
    global data
    data = board.next_iteration(data)
    im.set_array(data)
    return im,

ani = animation.FuncAnimation(fig, update)
plt.show()