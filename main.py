# Assignment: Image Colour Palette Generator
"""
A website that finds the most common colours in an uploaded image.
"""
import numpy

"""
One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.
https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.

On day 76, you learnt about image processing with NumPy. 
Using this knowledge and your developer skills (that means Googling), 
build a website where a user can upload an image and you will tell them 
what are the top 10 most common colours in that image.

This is a good example of this functionality:
http://www.coolphptools.com/color_extract#demo
"""
#TASKS:
"""
Just create a simple website to display the relevant info. Don't have to focus on design
Get the functionality working locally first - print statements (before exporting to website-- thr database? no need data persistence; only store on session)
1. Allow upload of specific image file
2. Process all colors using NumPy - Convert image to numpy array
3. Convert ndarray values to RGB? And pick out most common colors/array values?
    (Use mode/median/mean?)
    Store each array element in a list? 
    -Check for unique elements 
        ---How to compare 2 arrays? --> CONVERT TO STRING THEN COMPARE!!! (ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all())
        ---How to check if array is in list? https://stackoverflow.com/questions/53616706/how-to-check-if-an-array-is-in-a-list-of-arrays-in-python
    -Then calculate number of occurrences of each array element?
        ---Create dictionary to track count of different array elements
        ---How to add array as dictionary key value? -convert datatype to str
4. Choose top 10 # of array element occurrences to display as found colors
5. Display it on webpage; # of colors to display?
"""
"""
Python RGB image
NumPy Image Processing
NumPy Image Color Processing / color percentage in image/ detect background color of image / extract color from image
How to show image as nparray?/ Convert image into np array

ISSUE: Ran into a problem; solution takes forever to process all list elements; 
How to solve??? More complicated than u thought. No easy solution. Stuck on this for so long...

SOLUTION WORKS BUT TAKING FOREVER TO PARSE THROUGH ALL ELEMENTS; 
How to fix? Is there a better solution to compare array elements without adding all to new list?
How to process million of list elements???
>>use opencv?
>>Reduce dimension of image?? How to reduce dimension of image (PIL)?
"""

import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image

# Displaying array as image
# noise = np.random.random((128,128,3))
# print(noise.shape)
# print(numpy.ndarray)
# plt.imshow(noise)

#1.Allow choice of image
image = Image.open("TRMK.jpg")
print(image.size)
print(image.mode)

#2.Convert image to numpy array --- Already have whole image data (of each pixel--# of colors etc)
image_to_numpy = asarray(image)
print(image_to_numpy.shape)
print(image_to_numpy.ndim)

# print(image_to_numpy)

#2.1 Showing image (on Jupyter notebook only)
# plt.imshow(image_to_numpy)

#3.Convert ndarray values to RGB ? And pick out most common colors/array values?
# Store each array element in a list? Then calculate number of occurrences of each array element?

#R/G/B values respectively of each array element
print(image_to_numpy[0][0][0])
print(image_to_numpy[0][0][1])
print(image_to_numpy[0][0][2])

print(image_to_numpy[0][0]) #<---- this is what u r interested in; store all array elements then calc # of occurrence

#For array, height (x) and width (y) are flipped
print(image_to_numpy.shape[0]) #height/1325 #x
print(image_to_numpy.shape[1]) #width/2355 #y

print("Processing all array elements...")
array_elements = []
#Obtaining all image array elements
for i in range(image_to_numpy.shape[0]):
    for j in range(image_to_numpy.shape[1]):
        array_elements.append(str(image_to_numpy[i][j]))

#There should be 1325*2355 elements in whole dataset --- SOLUTION WORKS BUT TAKING FOREVER TO PARSE THROUGH ALL ELEMENTS
# print(array_elements[0])
# print(len(array_elements))
print("DONE PROCESSING...")

unique_elements = []
count_elements = {}
#Check for unique elements
for item in array_elements:
    print(item)
    if item not in unique_elements:
        unique_elements.append(item)
    # Create dictionary to track count of different array elements
    # eg: count_elements = {"a":1, "b":2, "c":3} ; where a,b,c = [r,g,b] array color element
    if item in count_elements:
        count_elements[item] += 1
    else:
        count_elements[item] =1

print("ANALYSING ARRAY ELEMENTS")
# print(unique_elements)
# print(len(unique_elements))
# print(count_elements)
# print(len(count_elements))


