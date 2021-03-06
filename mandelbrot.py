import matplotlib.pyplot as plt
import numpy as np


from mandel_function import mandelbrot


height=800
width=1200
iterations=100

re_0=-2
re_1=1
im_0=-1
im_1=1

c=complex(0,1)



import numpy as np
img=np.zeros((width,height))

for x in range(width):
    for y in range(height):
        c=complex(re_0+(x/width)*(re_1-re_0), im_0+(y/height)*(im_1-im_0))
        m=mandelbrot(c)
        m=255-int(255*m/iterations)
        img[x,y]=m

plt.imshow(img.T)
plt.show()


