import cv2
import numpy as np

def shape(s):
    img = cv2.imread(s)  
    cv2.imshow('original', img)   
    cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    edged = cv2.Canny(gray, 170, 255) 

    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    (contours, _) = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    def detectShape(c): 
        shape = 'unknown'
        peri = cv2.arcLength(c, True)
        vertices = cv2.approxPolyDP(c, 0.02 * peri, True)
        sides = len(vertices)
        if sides == 3:
            shape = 'triangle'
        elif sides == 4:
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = float(w) / h
            shape = 'square' if aspect_ratio == 1 else 'rectangle'
        elif sides == 5:
            shape = 'pentagon'
        elif sides == 6:
            shape = 'hexagon'
        elif sides == 7:
            shape = 'heptagon'
        elif sides == 8:
            shape = 'octagon'
        elif sides == 9:
            shape = 'nonagon'

        return shape


    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100];

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    result_image = img.copy()

    """for i, contour in enumerate(contours[:2]):
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(result_image, (cx, cy), 5, (255, 0, 0), -1)
        ###cv2.putText(result_image, f"Largest-{i+ 1}", (cx + 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)"""

    for cnt in contours:
        moment = cv2.moments(cnt)
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        shape = detectShape(cnt)
        cv2.drawContours(result_image, [cnt], -1, (0, 255, 0), 2)
        cv2.putText(result_image, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2) 
        cv2.imshow('polygons_detected', result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

shape("/Users/akashpaijwar/Documents/Winter Project/CV101/MS/4th part/types-of-regular-polygon.png")
