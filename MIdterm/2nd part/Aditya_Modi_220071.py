import cv2
import numpy as np

def hough_line(s):
    img = cv2.imread(s)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
   
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=105)
    
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x = a*rho
        y = b*rho
        x1 = int(x + 1000 * (-b))
        y1 = int(y + 1000 * (a))
        x2 = int(x - 1000 * (-b))
        y2 = int(y - 1000 * (a))
            
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    
    
    cv2.imshow("Lines", img)
    cv2.waitKey(0)

# Test
hough_line("/Users/akashpaijwar/Documents/Winter Project/CV101/MS/2nd part/white-notebook-pen-write.jpg")
