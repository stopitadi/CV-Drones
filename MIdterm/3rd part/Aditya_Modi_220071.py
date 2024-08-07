import cv2
import numpy as np

def colour(s):
    image = cv2.imread(s)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 0, 255), 2)
    cv2.imshow("Original Image", image)
    cv2.imshow("Detected Blue Shades", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage:
#s = "/Users/akashpaijwar/Documents/Winter Project/CV101/MS/3rd part/images.jpeg"
#colour(s)
