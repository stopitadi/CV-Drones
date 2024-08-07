from djitellopy import Tello
import cv2

# Step 1: Connecting to Tello drone
tello = Tello()
tello.connect()

# Step 2: Streaming video feed
tello.streamon()

# Step 3: Starting the drone
tello.takeoff()

# Step 4: Making it move 10cm left
tello.move_left(10)

# Display the video feed on the laptop screen
while True:
    # Get the frame from the video stream
    frame = tello.get_frame_read().frame

    # Display the frame
    cv2.imshow("Tello Video Stream", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cv2.destroyAllWindows()

# Land the drone
tello.land()

# Stop the video stream
tello.streamoff()
"""

from djitellopy import Tello
import cv2

# Step 1: Connecting to Tello drone

Tello.connect()

# Step 2: Streaming video feed
Tello.streamon()
# Display the video feed on the laptop screen
while True:
    # Get the frame from the video stream
    frame = tello.get_frame_read().frame

    # Display the frame
    cv2.imshow("Tello Video Stream", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 3: Starting the drone
Tello.takeoff()

# Step 4: Making it move 10cm left
Tello.move_left(10)
"""
