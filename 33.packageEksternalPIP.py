#menggunakan package eksternal python

#numphy package
import numpy as np

a = np.array([1 , 2 , 3 , 4])
b = np.array([5, 6 , 7, 8])

c = a+b
print(c)



#pillow package
from PIL import Image

im = Image.open("python.jpg")

print("format file = " + im.format)
print("ukuran file = " + str(im.size))
print("mode file = " + im.mode)