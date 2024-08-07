import cv2
#module that contains all image processing libraries

img = cv2.imread(r"/Users/akashpaijwar/Downloads/dice-1502706_640.jpg")
#display the image
#bluring the image

img2 = cv2.blur(img, (5,5))
cv2.imshow('Image',img2)
#name of window and variable which it store
cv2.waitKey(0)#delay time for image

#convert in to gray scale
img1=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#syntax to flip an image
img2 = cv2.flip(img,0)

#first assignment
import cv2
import numpy as np

def solve(s):
    img = cv2.imread(r"s")
    img1 =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    f = np.fft.fft2(img_gray)
    fshift = np.fft.fftshift(f)
    mag = 20* np.log(np.abs(fshift))


    magnitude_spectrum = np.uint8(mag)
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum)
    cv2.waitKey(0)
