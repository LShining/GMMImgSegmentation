import matplotlib.pyplot as plt
from scipy import misc
R = 0
G = 1
B = 2
img = misc.imread('TestImage.jpg')
for pixelRow in img:
    for pixel in pixelRow:
        try:
            r = pixel[R]/(float(pixel[R])+pixel[G]+pixel[B])
        except ZeroDivisionError:
            r = 0
        try:
            g = pixel[G]/(float(pixel[R])+pixel[G]+pixel[B])
        except ZeroDivisionError:
            g = 0
        alpha = 255/(max([r,g,1-r-g]))
        pixel[R] = int(alpha*r)
        pixel[G] = int(alpha*g)
        pixel[B] = int(alpha*(1-r-g))
misc.imsave('poi.jpg' , misc.toimage(img))
