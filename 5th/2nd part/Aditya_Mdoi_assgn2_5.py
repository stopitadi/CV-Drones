import cv2
import numpy as np

# Global variable to store the generated Indian flag
generated_indian_flag = None

def generate():
    global generated_indian_flag
    
    # White canvas of size 600x600
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

    generated_indian_flag = indian_flag
    return indian_flag

# Global variables to store rotated Indian flags
rotated_flag_0_deg = None
rotated_flag_90_deg = None
rotated_flag_180_deg = None
rotated_flag_270_deg = None

def rotate(img, angle):
    # Get image center and rotation matrix
    center = tuple(np.array(img.shape[1::-1]) / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply rotation to the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    return rotated_img

def rotatedFlags():
    global rotated_flag_0_deg, rotated_flag_90_deg, rotated_flag_180_deg, rotated_flag_270_deg, generated_indian_flag
    flag = generate()

    # Rotating the Indian Flag at different angles
    flag_0_deg = flag
    flag_90_deg = rotate(flag, 90)
    flag_180_deg = rotate(flag, 180)
    flag_270_deg = rotate(flag, 270)

    # Display the rotated flags (optional)
    cv2.imshow('Rotated Flag 0 Degrees', flag_0_deg)
    cv2.imshow('Rotated Flag 90 Degrees', flag_90_deg)
    cv2.imshow('Rotated Flag 180 Degrees', flag_180_deg)
    cv2.imshow('Rotated Flag 270 Degrees', flag_270_deg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Displaying Rotated images
rotatedFlags()
