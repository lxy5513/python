import matplotlib
matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import cv2

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

fig, axes = plt.subplots(nrows=6)

fig.show()

# We need to draw the canvas before we start animating...
fig.canvas.draw()

styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']

def plot(ax, style):
    #  return ax.plot(x, y, style, animated=True)[0]
    return ax.plot(x, y, style)[0]

lines = [plot(ax, style) for ax, style in zip(axes, styles)]

# Let's capture the background of the figure
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

tstart = time.time()
for i in range(1, 200):
    items = enumerate(zip(lines, axes, backgrounds), start=1)
    for j, (line, ax, background) in items:
        fig.canvas.restore_region(background)
        line.set_ydata(np.sin(j*x + i/10.0))
        ax.draw_artist(line)
        width, height = fig.get_size_inches() * fig.get_dpi() 
        image = np.fromstring(fig.canvas.tostring_rgb(), dtype='uint8').reshape(int(height), int(width), 3)
        cv2.imshow('im', image) 
        cv2.waitKey(3)
        #  fig.canvas.blit(ax.bbox)
        #  import ipdb;ipdb.set_trace()


print('FPS:' , 200/(time.time()-tstart))
