import matplotlib.pyplot as plt
from scipy import misc
R = 0
G = 1
B = 2
img = misc.imread('face.png')
for pixelRow in img:
    for pixel in pixelRow:
        pixel[B] = 0
misc.imsave('poi.jpg' , misc.toimage(img))
