import cv2
import numpy as np
import matplotlib.pyplot as plt

def ig_filter(s):
    img = cv2.imread(s)
    #Reduce brightness to 0.5 of its initial value
    bright = cv2.convertScaleAbs(img, alpha=0.5, beta=0.5)
    #Increasing contrast to 1.5 of its initial value
    contrast = cv2.convertScaleAbs(bright, alpha=1.5, beta=0)
    #Increasing saturation to 1.5 of its initial value
    rgb = cv2.cvtColor(contrast, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255)
    img_saturation = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    #The final filtered image
    plt.imshow(img_saturation)
    plt.title("Final Filtered Image")
    plt.axis('off')
    plt.show()

    return img_saturation

#Test
#s = "/Users/akashpaijwar/Documents/Winter Project/CV101/MS/1st part/SOln/cherrytree.jpeg"
#g_filter(s)
