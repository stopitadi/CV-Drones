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
    rotated_flag_0_deg = flag
    rotated_flag_90_deg = rotate(flag, 90)
    rotated_flag_180_deg = rotate(flag, 180)
    rotated_flag_270_deg = rotate(flag, 270)

# Combine unskew function
def is_black_or_blue(color):
    threshold = 50
    return all(c < threshold for c in color)

def unskew(s):
    global unskewed_image, rotated_flag_0_deg, rotated_flag_90_deg, rotated_flag_180_deg, rotated_flag_270_deg
    
    image = cv2.imread(s)

    if image is None:
        print(f"Failed to load the image at path: {s}")
        return

    image_height, image_width, _ = image.shape

    vertical_colors = []

    mid_col = image_width // 2
    for i in range(image_height):
        color = tuple(image[i, mid_col])
        if not is_black_or_blue(color) and color not in vertical_colors:
            vertical_colors.append(color)

    num_colors = len(vertical_colors)
    third = num_colors // 3

    top_section = vertical_colors[:third]
    middle_section = vertical_colors[third:2 * third]
    bottom_section = vertical_colors[2 * third:]

    avg_color_top = np.mean(top_section, axis=0)
    avg_color_middle = np.mean(middle_section, axis=0)
    avg_color_bottom = np.mean(bottom_section, axis=0)

    if not all(avg_color_top) or not all(avg_color_middle) or not all(avg_color_bottom):
        print("One or more sections have no valid colors.")
        return

    max_avg_color_top = np.argmax(avg_color_top)
    max_avg_color_middle = np.argmax(avg_color_middle)
    max_avg_color_bottom = np.argmax(avg_color_bottom)

    if max_avg_color_top == 0 and max_avg_color_middle == 0 and max_avg_color_bottom == 0:
        horizontal_colors = []
        mid_row = image_height // 2
        for j in range(image_width):
            color = tuple(image[mid_row, j])
            if not is_black_or_blue(color) and color not in horizontal_colors:
                horizontal_colors.append(color)

        num_horizontal_colors = len(horizontal_colors)
        third_horizontal = num_horizontal_colors // 3

        left_section = horizontal_colors[:third_horizontal]
        center_section = horizontal_colors[third_horizontal:2 * third_horizontal]
        right_section = horizontal_colors[2 * third_horizontal:]

        avg_color_left = np.mean(left_section, axis=0)
        avg_color_center = np.mean(center_section, axis=0)
        avg_color_right = np.mean(right_section, axis=0)

        if not all(avg_color_left) or not all(avg_color_center) or not all(avg_color_right):
            print("One or more horizontal sections have no valid colors.")
            return

        red_channel_position_horizontal = np.argmax(avg_color_left)

        if red_channel_position_horizontal == 2:
            unskewed_image = rotated_flag_90_deg
        else:
            unskewed_image = rotated_flag_270_deg
    else:
        red_channel_position = np.argmax(avg_color_top)

        if red_channel_position == 2:
            unskewed_image = rotated_flag_0_deg
        else:
            unskewed_image = rotated_flag_180_deg

    # Display the unskewed image
    cv2.imshow("Unskewed Image", unskewed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call rotatedFlags to generate rotated flag images
rotatedFlags()




unskew("5th/3rd part/testcase/WhatsApp Image 2023-12-25 at 21.19.32.jpeg")
