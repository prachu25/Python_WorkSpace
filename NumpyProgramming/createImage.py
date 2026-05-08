# pip installl numpy          open numpy folder on command prompt
# pip install pillow       -> enter this command on - command prompt : on Numpyfolder like that way      PS C:\Users\ASUS\Desktop\Python_Works\Numpy> python .\createImage.py

import numpy
from PIL import Image 

# create a graysacle image 
img = numpy.zeros((100,100), dtype=numpy.uint8)

for i in range(100):
    for j in range(100):
        img[i,j]=i+j


image = Image.fromarray(img)
image.save("gradient.png")

print('image saved...')