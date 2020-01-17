import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import numpy as np
import time
import cv2
from tqdm import tqdm 

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#  fig.show()
fig.canvas.draw()

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
styles = ['r-', 'g-']

def plot1(ax, style, text):
    ax.plot(x, y, style)
    ax.legend(text)
    return ax

def plot2(ax, style, text):
    ax.plot(x, y, style)
    ax.legend(text)
    return ax
axes = [ax1, ax2]
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

tstart = time.time()
for i in tqdm(range(1, 200)):
    items = enumerate(zip(axes, backgrounds), start=1)
    for j, (ax, background) in items:
        #  import ipdb;ipdb.set_trace()
        if j == 1:
            fig.canvas.restore_region(background)
            ax.draw_artist(plot1(ax, styles[0], 'image 1'))
            #  plot1(ax, styles[0], 'image 1')
            #  fig.canvas.blit(ax.bbox)
        else:
            fig.canvas.restore_region(background)
            ax.draw_artist(plot2(ax, styles[1], 'image2'))
            #  fig.canvas.blit(ax.bbox)
            #  plot2(ax, styles[1], 'image2')
    width, height = fig.get_size_inches() * fig.get_dpi() 
    image = np.fromstring(fig.canvas.tostring_rgb(), dtype='uint8').reshape(int(height), int(width), 3)
    #  cv2.imshow('im', image) 
    #  cv2.waitKey(3000)
    #  import ipdb;ipdb.set_trace()
    fig.canvas.blit(ax.bbox)

print('FPS:' , 200/(time.time()-tstart))
