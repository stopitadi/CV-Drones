import cv2
import numpy as np

# Global variable to store the generated Indian flag (from previous question)
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

# Call the generate function to create the Indian flag
generate()

def unskew(s):
    # Read the input skewed image
    skewed_image = cv2.imread(s)
    if skewed_image is None:
        raise ValueError(f"Failed to load the image at path: {s}")


    # Get the height of the input image
    image_height = skewed_image.shape[0]

    # Determine the midline position based on the actual image size
    midline_position = image_height // 2

    # Create a blank reference image
    reference_image = np.ones((image_height, skewed_image.shape[1], 3), dtype=np.uint8) * 255  # Blank canvas

    # Perform vertical traversal along the midline
    midline_colors = [tuple(skewed_image[i, midline_position]) for i in range(image_height)]

    # Store distinct colors (excluding blue and black) in an array called vertical
    vertical = list(set(midline_colors) - {(255, 0, 0), (0, 0, 0)})

    # Identify Key Colors
    key_colors = [color for color in vertical if color not in [(255, 0, 0), (0, 0, 0)]]

    # Color Correction
    corrected_image = skewed_image.copy()

    for key_color in key_colors:
        if key_color == (0, 128, 0):  # Example, replace green color
            corrected_image[np.all(corrected_image == key_color, axis=-1)] = [0, 128, 0]  # RGB color for green
        elif key_color == (255, 255, 255):  # Example, replace white color
            corrected_image[np.all(corrected_image == key_color, axis=-1)] = [255, 255, 255]  # RGB color for white
        elif key_color == (0, 165, 255):  # Example, replace saffron color
            corrected_image[np.all(corrected_image == key_color, axis=-1)] = [0, 165, 255]  # RGB color for saffron

    # Generate Reference Image
    for i in range(image_height):
        for j in range(skewed_image.shape[1]):
            reference_image[i][j] = corrected_image[i][j]

    # Display the Reference Image
    cv2.imshow('Reference Image', reference_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Replace 'path/to/your/image.jpg' with the actual path of your input image




unskew('/Users/akashpaijwar/Documents/Winter Project/CV101/5th/3rd part/testcase/2.jpeg')
