# -*- coding: utf-8 -*-
"""CARTOONIZING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JlqDh9nb_RePDZKBlzfVINYmdLh4nyBT

we heared about the filters,like anything on the snapchat or we also have this pixar where in we provide any input image and you know we get this edges and its something we try to cartonify the image.so similar thing is what we are going to do here using python and library that using the "opencv2" 1.loading the image 2.creating the mask 3.reducing the noise 4.reducing the colour palette(cartoon which have only four number of colours) 5.finally we can combine the edge mask and colour palette

-->mainly e=we using the opencv2 and some standard libraries are the matplotlib.
"""

#import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""image loading

loading images using the function when the files are read using cv2 they are usually read into the bgr format and we need to convert into the rgb




img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
in the img equal to the cv2.cvtcolor mean convert into the colour of the BGR to the RGB(into the binary part) 
"""

#loading the images
#for loading the images here using the function and defining the function i.e read_file
#filename- is the pathname
def read_file(filename):
  img=cv2.imread(filename)
  img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #converting from bgr to rgb
  plt.imshow(img)# to see the image
  #plt.axes('off')#to off the axis to the image
  plt.show()
  return img #returns the binary part

"""we are getting the array because above we return the img i.e the binary part so we get the array as the result """

filename="image.jpg" #assigning the image to the variable filename as the string
read_file(filename) #function call

"""in below we get the only img not the array because we equal the function call to the img."""

filename="image.jpg" #assigning the image to the variable filename as the string
img = read_file(filename)

filename="image.jpg" #assigning the image to the variable filename as the string
img = read_file(filename) #function call

org_img = np.copy(img)

"""here we are increasing the edges of our image over here.we have the adaptive threshold in opencv2 hich help us,so define the function edge_mask and taken input as the img , size of the mask is the-line_size ,value is the-blur_val


-->convert our image from RGB to the gray





##create edge mask
"""

def edge_mask(img,line_size,blur_value):
  """
  input:INPUT Image
  Output:Edges of images
  """
  gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)#converting our img from RGB to the gray
  gray_blur=cv2.medianBlur(gray,blur_value) #converting to gray_blur by using the median blur and gray image,blur_value
  edges=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,line_size,blur_value) #255-adaptive method,adaptive thresh mean is the built in function
  return edges

line_size,blur_value=7,7
edge_mask(img,line_size,blur_value)#calling the edge_mask function

line_size,blur_value=7,7
edges=edge_mask(img,line_size,blur_value)

line_size,blur_value=7,7
edge_mask(img,line_size,blur_value)

plt.imshow(edges)# to show that edges
plt.show()

"""by reducing the line_size we can decrease the thickness of edge of the image"""

line_size,blur_value=7,7
edge_mask(img,line_size,blur_value)

plt.imshow(edges , cmap = 'gray')# to show that edges in gray
plt.show()

line_size,blur_value=5,7
edge_mask(img,line_size,blur_value)

plt.imshow(edges,cmap = 'binary')# to show that edges
plt.show()

"""now reducing the color palette that mean the in original image we have the many colors so we want only three colors that is reducing the no.of colors.for that we are going to create a function is color_quantization and giving input as the image 
k= refers to the no.of colors u want
    that mean no.of centriods


##reducing the color palatee
"""

def color_quantization(img,k):
  #Transformation of image
  data=np.float32(img).reshape((-1,3)) #that mean reshaping the image
  #Determine criteria
  criteria=(cv2.TERM_CRITERIA_EPS+cv2.TermCriteria_MAX_ITER,20,0.001)
  ##Implementing K-means
  ret,label,center=cv2.kmeans(data,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
  center=np.uint8(center)
  result=center[label.flatten()]
  result=result.reshape(img.shape)
  return result

img = color_quantization(img,k = 2)

img = color_quantization(img,k = 2)
plt.imshow(img)
plt.show()

img_quant = color_quantization(img,k = 2)
plt.imshow(img)
plt.show()

img_quant = color_quantization(img,k = 5)
plt.imshow(img)
plt.show()

img = color_quantization(img,k = 1)
plt.imshow(img)
plt.show()

"""
-->for reducing the noise we need to pass throught the filter"""

#reduce the noise
#filter-bilateralfilter
#diameter of img - 7
#sigmacolor - 200
blurred=cv2.bilateralFilter(img,d=7,sigmaColor=200,sigmaSpace=200)
plt.imshow(blurred)
plt.show()

"""cobine the edge mask with the quantize image"""

def cartoon():
  c=cv2.bitwise_and(blurred,blurred,mask=edges)

  plt.imshow(c)
  plt.title("cartoonified image")
  plt.show() 

  plt.imshow(org_img)
  plt.title("org_img")
  plt.show()

cartoon()

#change the d, k , line_size values to see the changes in the images.