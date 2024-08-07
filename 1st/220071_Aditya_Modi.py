import cv2
import numpy as np

def solve(s):
    img = cv2.imread(s)        # Read the image
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    # Convert the image to BW
    f = np.fft.fft2(img_gray)        # Computing Fourier Transform
    magnitude_spectrum = 20*np.log(np.abs(f)) 
    magnitude_spectrum = np.uint8(magnitude_spectrum) 
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum)
    cv2.waitKey(0)

#Testing the function
image_path = "/Users/akashpaijwar/Documents/Winter Project/CV101/MS/1st part/SOln/cherrytree.jpeg"

solve(image_path)
  

