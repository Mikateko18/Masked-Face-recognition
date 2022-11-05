from PIL import Image
import cv2
from flask import render_template, request
from flask import redirect, url_for
import os
import glob
from cv2 import threshold
import numpy as np
from numpy import linalg as la
from pylab import *
import matplotlib.pyplot as plt 

training_images_directory = "static/uploads"
images = os.listdir(training_images_directory)

for count, imageName in enumerate(images,1):
  image = plt.imread(os.path.join(training_images_directory,imageName))

def getLocalBinaryPatternImage(grayImage):
  imageLocalBinaryPattern = np.zeros_like(grayImage)
  neighboor = 3
  for imageHeight in range(0,image.shape[0] - neighboor):
    for imageWidth in range(0,image.shape[1] - neighboor):
      images          = grayImage[imageHeight:imageHeight+neighboor,imageWidth:imageWidth+neighboor]
      center       = images[1,1]
      image01        = (images >= center)*1.0
      image01Vector = image01.T.flatten()
      image01Vector = np.delete(image01Vector,4)
      whereImage01Vector = np.where(image01Vector)[0]
      if len(whereImage01Vector) >= 1:
        num = np.sum(2**whereImage01Vector)
      else:
        num = 0
      imageLocalBinaryPattern[imageHeight+1,imageWidth+1] = num
  
  return(imageLocalBinaryPattern)
  

training_images_directory  = "static/uploads"
images = os.listdir(training_images_directory )
for imageName in images:
  image = plt.imread(os.path.join(training_images_directory ,imageName))
  imageLocalBinaryPattern    = getLocalBinaryPatternImage(image)
  vecimgLBP = imageLocalBinaryPattern.flatten()
  figure = plt.figure(figsize=(22,10))
  axis  = figure.add_subplot(1,3,1)
  axis.imshow(image)
  axis.set_title(imageName)
  axis  = figure.add_subplot(1,3,2)
  axis.imshow(imageLocalBinaryPattern)
  axis.set_title("Local Binary Pattern converted image")
  axis  = figure.add_subplot(1,3,3)
  freq,localBinaryPattern, _ = axis.hist(vecimgLBP,bins=2**8)
  axis.set_ylim(0,40000)
  localBinaryPattern = localBinaryPattern[:-1]
  largeTF = freq > 5000
  
  axis.set_title("Local Binary Pattern histogram")
  plt.savefig( './static/LBPImages/'+ imageName)
 

  