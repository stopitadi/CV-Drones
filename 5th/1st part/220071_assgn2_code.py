import cv2
import numpy as np

generated_indian_flag = None

def generate():
    global generated_indian_flag
    
    #White canvas of size 600x600
    indian_flag = np.ones((600, 600, 3), dtype=np.uint8) * 255
    center = (300, 300)
    radius = 100
    chakra_width = 2
    spoke_width = 1

    # Green part
    cv2.rectangle(indian_flag, (0, 400), (600, 600), (0, 128, 0), thickness=cv2.FILLED)

    cv2.rectangle(indian_flag, (0, 200), (600, 300), (255, 255, 255), thickness=cv2.FILLED)

    # Orange part
    cv2.rectangle(indian_flag, (0, 0), (600, 200), (0, 165, 255), thickness=cv2.FILLED)

    # The blue circle (chakra)
    cv2.circle(indian_flag, center, radius, (255, 0, 0), thickness=chakra_width)

    # Draw the 24 spokes
    num_spokes = 24
    for i in range(num_spokes):
        angle = i * (360 / num_spokes)
        endpoint_x = int(center[0] + radius * np.cos(np.radians(angle)))
        endpoint_y = int(center[1] + radius * np.sin(np.radians(angle)))
        cv2.line(indian_flag, center, (endpoint_x, endpoint_y), (255, 0, 0), thickness=spoke_width)

    cv2.imshow('Generated Indian Flag', indian_flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    generated_indian_flag = indian_flag
#Display Test
generate()
