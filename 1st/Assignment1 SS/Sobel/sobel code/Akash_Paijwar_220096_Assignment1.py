import cv2
import numpy as np
import matplotlib.pyplot as plt

def Sobel(s):
    img = cv2.imread(s)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=1)
    y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=1)
    
    magnitude = np.sqrt(x**2 + y**2)

    mag = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    plt.subplot(1, 2, 1)
    plt.imshow(img[:,:,::-1])
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(mag, cmap='gray')
    plt.title('Sobel Filter')
    plt.axis('off')

    plt.show()



# Test
#Sobel("/Users/akashpaijwar/Documents/Winter Project/CV101/1st/Assignment1 SS/Sobel/images (1).jpeg")
