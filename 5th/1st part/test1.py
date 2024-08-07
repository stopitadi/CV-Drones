import cv2
import numpy as np

# Global variable to store the generated Indian flag
indian_flag = None

def generate():
    global indian_flag
    
    # Create a blank white canvas for the flag
    flag_height, flag_width = 600, 600
    indian_flag = np.ones((flag_height, flag_width, 3), dtype=np.uint8) * 255

    # Draw the green rectangle (lower part of the flag)
    green_height = flag_height // 3
    indian_flag[2 * green_height:, :] = [0, 128, 0]  # RGB color for green

    # Draw the white rectangle (middle part of the flag)
    white_height = flag_height // 3
    indian_flag[green_height:2 * green_height, :] = [255, 255, 255]  # RGB color for white

    # Draw the saffron rectangle (upper part of the flag)
    indian_flag[:green_height, :] = [0, 165, 255]  # RGB color for saffron

    # Draw the blue circle (chakra)
    center = (300, 300)
    radius = 100
    thickness = 2
    cv2.circle(indian_flag, center, radius, [255, 0, 0], 2)

    # Draw the 24 spokes
    num_spokes = 24  # You can adjust this number as needed
    for i in range(num_spokes):
        angle = i * (360 / num_spokes)
        x1 = center[0] 
        y1 =center[1] 
        x2 = int(center[0] + (radius ) * np.cos(np.radians(angle)))
        y2 = int(center[1] + (radius ) * np.sin(np.radians(angle)))
        cv2.line(indian_flag, (x1, y1), (x2, y2), [255, 0,0 ], 1)

    # Display the generated Indian flag
    cv2.imshow('Indian Flag', indian_flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the generate function to generate and display the Indian flag
#generate()
# Global variables to store rotated Indian flags
rotated_flag_0 = None
rotated_flag_90 = None
rotated_flag_180 = None
rotated_flag_270 = None

def rotate(img, angle):
    """
    Rotates the given image 'img' at an angle of 'angle' degrees.
    Rotation is performed in the anticlockwise direction.

    Parameters:
    - img: Input image
    - angle: Angle of rotation in degrees

    Returns:
    - Rotated image
    """
    height, width = img.shape[:2]
    center = (width // 2, height // 2)

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation to the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    return rotated_img

def rotatedFlags():
    global rotated_flag_0, rotated_flag_90, rotated_flag_180, rotated_flag_270

    # Create the original Indian flag
    generate()

    # Rotate the original flag at different angles
    rotated_flag_0 = indian_flag.copy()
    rotated_flag_90 = rotate(indian_flag, 90)
    rotated_flag_180 = rotate(indian_flag, 180)
    rotated_flag_270 = rotate(indian_flag, 270)

    # Display the rotated flags
    cv2.imshow('Rotated Flag 0 Degrees', rotated_flag_0)
    cv2.imshow('Rotated Flag 90 Degrees', rotated_flag_90)
    cv2.imshow('Rotated Flag 180 Degrees', rotated_flag_180)
    cv2.imshow('Rotated Flag 270 Degrees', rotated_flag_270)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the rotatedFlags function to generate and display all four orientations of the Indian flag
rotatedFlags()
