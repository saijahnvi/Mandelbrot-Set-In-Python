#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import numba 

def mandelbrot(z0,n):
  z=complex(0,0)
  for i in range(0,n):
    if abs(z)>2:
      return i
    else:
      z=z*z+z0

  return n

nx=1000
ny=1000
maxsteps=1000
ext=[-2,1,-1,1]
colormap='magma'
mand=np.zeros((ny,nx)) 

for i in range(0,nx):
  for j in range(0,ny):
    x=ext[0]+(ext[1]-ext[0])*i/(nx-1)
    y=ext[2]+(ext[3]-ext[2])*j/(ny-1)
    mand[j, i] = mandelbrot(complex(x, y), maxsteps)

ax = plt.axes()
ax.set_aspect('equal')

graph = ax.imshow(mand, extent=ext, cmap=colormap, origin='lower', interpolation='bilinear')
plt.colorbar(graph)
plt.xlabel("Real-Axis")
plt.ylabel("Imaginary-Axis")
plt.gcf().set_size_inches(5, 4)
plt.tight_layout()  
plt.show()
