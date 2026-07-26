import numpy as np
from numba import jit
import time
from pylab import*
import matplotlib.pyplot as plt
from scipy import*
@jit(nopython=True)
def mandelbrot(ext,maxsteps,nx,ny):
    data=np.ones((ny,nx))*maxsteps
    
    for i in range(0,nx):
        for j in range(0,ny):
            x=ext[0]+(ext[1]-ext[0])*i/(nx-1)
            y=ext[2]+(ext[3]-ext[2])*j/(ny-1)
            z0=x+y*1j
            z=0j
            for itr in range(0,maxsteps):
                if abs(z)>2:
                    data[j,i]=itr
                    break
                z=z*z + z0
    return data

def ax_update(ax):
    ax.set_autoscale_on(False)
   
    xstart,ystart,xdelta,ydelta=ax.viewLim.bounds 
    xend= xstart + xdelta
    yend= ystart + ydelta
    ext=[xstart,xend,ystart,yend]
    data=mandelbrot(array(ext),maxsteps,nx,ny)
   
    im=ax.images[-1]
    im.set_data(data)
    im.set_extent(ext)
    ax.figure.canvas.draw_idle()




nx=1000
ny=1000
maxsteps=500
ext=[-2,1,-1,1]
t0 = time.time()
data = mandelbrot(array(ext),maxsteps,nx,ny)
t1 = time.time()
print ('Python ',t1-t0,'s')
fig,ax=subplots(1,1)


ax.imshow(data,extent=ext,aspect='equal',origin='lower')
ax.callbacks.connect('xlim_changed',ax_update) #maybe you are passing only one axis when u specify the argument and hence we give no arguments
ax.callbacks.connect('ylim_changed',ax_update)
show()
