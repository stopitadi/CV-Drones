import cv2
import numpy as np

# Global variables for rotated flags
rotated_flag_0_deg = None
rotated_flag_90_deg = None
rotated_flag_180_deg = None
rotated_flag_270_deg = None

# Global variable for unskewed image
unskewed_image = None

def rotate(img, angle):
    # Get image center and rotation matrix
    center = tuple(np.array(img.shape[1::-1]) / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply rotation to the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    return rotated_img

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

def unskew(s):
    global rotated_flag_0_deg, rotated_flag_90_deg, rotated_flag_180_deg, rotated_flag_270_deg, unskewed_image

    # Read the input image
    input_image = cv2.imread(s)

    # Rotate the input image at different angles
    rotated_image_0_deg = input_image
    rotated_image_90_deg = rotate(input_image, 90)
    rotated_image_180_deg = rotate(input_image, 180)
    rotated_image_270_deg = rotate(input_image, 270)

    # Assuming that the rotated flags are already generated as global variables
    # rotated_flag_0_deg, rotated_flag_90_deg, rotated_flag_180_deg, rotated_flag_270_deg

    # Choose the rotated flag that matches the input image orientation
    # You may need to compare and choose the best match based on some criteria
    # For simplicity, let's assume that 0-degree rotation is the correct orientation
    reference_flag = rotated_flag_0_deg

    # Define the source points (coordinates of the skewed input image)
    source_points = np.array([[0, 0], [599, 0], [599, 599], [0, 599]], dtype=np.float32)

    # Define the destination points (coordinates of the reference flag)
    destination_points = np.array([[0, 0], [599, 0], [599, 599], [0, 599]], dtype=np.float32)

    # Calculate the affine transformation matrix
    affine_matrix = cv2.getAffineTransform(source_points, destination_points)

    # Apply the affine transformation to correct the image
    unskewed_image = cv2.warpAffine(input_image, affine_matrix, (600, 600))

    # Display the unskewed image
    cv2.imshow("Unskewed Image", unskewed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

   
    
# Sample input file path
input_image_path = "/Users/akashpaijwar/Documents/Winter Project/CV101/5th/3rd part/testcase/2.jpeg"

# Call the functions to generate the flag, perform vertical traversal, and display the reference image

# Call the unskew function
unskew(input_image_path)
