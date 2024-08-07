import cv2
import cv2.aruco as aruco
import numpy as np

def markers(s):
    # Read the input image
    img = cv2.imread(s)
    if img is None:
        print(f"Error: Unable to read the image at path: {s}")
        return

    # Define the ArUco dictionary and parameters
    arucoDict = cv2.aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()

    # Camera matrix and distortion coefficients
    cameraMatrix = np.array([[1.29498043e+03, 0.00000000e+00, 8.99709858e+02],
                             [0.00000000e+00, 1.28247438e+03, 4.38989960e+02],
                             [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    distCoeffs = np.array([[-0.26789405, 0.1998461, 0.01383549, 0.01250974, -0.13353454]])

    # Detect ArUco markers in the image
    corners, ids, _ = aruco.detectMarkers(img, arucoDict, parameters=parameters)

    if ids is not None and len(ids) > 0:

        aruco.drawDetectedMarkers(img, corners, ids)

        # Calculate pose information for the detected marker
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 0.1, cameraMatrix, distCoeffs)

        # Retrieve translation and rotation vectors for the first marker (assuming only one marker is present)
        rvec = rvecs[0]
        tvec = tvecs[0]

        # Compute the center of the marker
        xc, yc = np.mean(corners[0][0], axis=0)
        x0, y0 = img.shape[1] // 2, img.shape[0] // 2  # Assuming img is the captured frame


        # Compute the pose axes (x, y, z axes)
        axis_length = 0.05  # Length of the axes
        axis_points = np.float32([[0, 0, 0], [axis_length, 0, 0], [0, axis_length, 0], [0, 0, axis_length]]).reshape(-1, 3, 1)
        image_points, _ = cv2.projectPoints(axis_points, rvec, tvec, cameraMatrix, distCoeffs)

        # Draw the pose axes
        pt1 = tuple(map(int, image_points[0].ravel()))
        pt2 = tuple(map(int, image_points[1].ravel()))
        img = cv2.line(img, pt1, pt2, (255, 0, 0), 4)

        pt1 = tuple(map(int, image_points[0].ravel()))
        pt2 = tuple(map(int, image_points[2].ravel()))
        img = cv2.line(img, pt1, pt2, (0, 255, 0), 4)

        pt1 = tuple(map(int, image_points[0].ravel()))
        pt2 = tuple(map(int, image_points[3].ravel()))
        img = cv2.line(img, pt1, pt2, (0, 0, 255), 4)

        # Display the image with the detected marker and pose information
        cv2.imshow("Detected Marker", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return xc, yc, rvec, tvec,x0,y0
    else:
        print("No ArUco marker detected in the image.")
        return None

# Example usage:
markers_result = markers('/Users/akashpaijwar/Documents/Winter Project/CV101/5th/UD/Cali/0.png')
if markers_result is not None:
    xc, yc, rvec, tvec ,x0,y0= markers_result
    print(f"Center of the marker: ({xc}, {yc})")
    print(f"Rotation vector: {rvec}")
    print(f"Translation vector: {tvec}")
    # Calculate deviations
    Δx = xc - x0
    Δy = yc - y0

    # Display the deviations
    deviations = (Δx, Δy)
    print("Deviations:", deviations)
