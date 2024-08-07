import cv2
import matplotlib.pyplot as plt

def solve(s):
    img = cv2.imread(s, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150) 
    plt.figure(figsize=[10, 10])
    plt.imshow(edges, cmap="gray")
    plt.title("Canny Edge Detection")
    plt.show()


#test
#image_path = "/Users/akashpaijwar/Downloads/post-thumbnail.png"
#solve(image_path)
