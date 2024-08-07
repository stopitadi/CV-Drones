import cv2
import numpy as np

# Create a blank image with a white background
flag = np.ones((600, 600, 3), dtype=np.uint8) * 255

# Draw the saffron color portion of the flag
flag[0:200, :] = (0, 153, 255)

# Draw the white color portion of the flag
flag[200:400, :] = (255, 255, 255)

# Draw the green color portion of the flag
flag[400:600, :] = (19, 136, 8)

# Draw the blue circle (chakra) in the center of the flag
center = (300, 300)
radius = 100
thickness = 2
cv2.circle(flag, center, radius, (0, 0, 255), thickness)

# Draw the spokes of the chakra
num_spokes = 24
angle = 360 / num_spokes
spoke_width = 1
for i in range(num_spokes):
    start_point = (int(center[0] + radius * np.cos(np.radians(i * angle))),
                   int(center[1] + radius * np.sin(np.radians(i * angle))))
    end_point = (int(center[0] + radius * np.cos(np.radians((i * angle) + angle))),
                 int(center[1] + radius * np.sin(np.radians((i * angle) + angle))))
    cv2.line(flag, start_point, end_point, (0, 0, 255), spoke_width)

# Display the flag
cv2.imshow("Indian Flag", flag)
cv2.waitKey(0)
cv2.destroyAllWindows()