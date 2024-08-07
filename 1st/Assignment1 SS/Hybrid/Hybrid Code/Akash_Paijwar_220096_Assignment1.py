import cv2
import numpy as np
import matplotlib.pyplot as plt

def hybrid(s1,s2):
    # Load your images here
    img01 = cv2.imread("/Users/akashpaijwar/Downloads/download.jpeg")
    img02 = cv2.imread("/Users/akashpaijwar/Downloads/download (1).jpeg")

    img1=cv2. cvtColor (img01, cv2. COLOR_BGR2GRAY)
    img2=cv2. cvtColor (img02, cv2. COLOR_BGR2GRAY)

    # Resize images to [256, 256]
    img1 = cv2.resize(img1, (256, 256))
    img2 = cv2.resize(img2, (256, 256))

    # Fourier Transform
    f1 = np.fft.fft2(img1)
    Fshift1 = np.fft.fftshift(f1)

    plt.imshow(np.log1p(np.abs(Fshift1)), cmap='gray')
    plt.axis('off')
    plt.show()

    f2 = np.fft.fft2(img2)
    Fshift2 = np.fft.fftshift(f2)

    plt.imshow(np.log1p(np.abs(Fshift2)), cmap='gray')
    plt.axis('off')
    plt.show()      

    # Rectangular Low pass filter
    M, N = img1.shape
    H_lowpass = np.zeros((M, N), dtype=np.float32)

    # Set the dimensions of the rectangular low-pass filter
    rectangular_width = 30
    rectangular_height = 30

    # Low Pass Filter
    H_lowpass[
    M // 2 - rectangular_height // 2 : M // 2 + rectangular_height // 2,
    N // 2 - rectangular_width // 2 : N // 2 + rectangular_width // 2
    ] = 1

    plt.imshow(H_lowpass, cmap='gray')
    plt.axis('off')
    plt.show()  

    # Apply Rectangular Low Pass Filter
    Gshift_lowpass = Fshift1 * H_lowpass
    plt.imshow(np.log1p(np.abs(Gshift_lowpass)), cmap='gray')
    plt.axis('off')
    plt.show()

    # High Pass Filter
    H_highpass = 1 - H_lowpass

    plt.imshow(H_highpass, cmap='gray')
    plt.axis('off')
    plt.show()

    #Apply Rectangular High Pass Filter
    Gshift_highpass = Fshift2 * H_highpass
    plt.imshow(np.log1p(np.abs(Gshift_highpass)), cmap='gray')
    plt.axis('off')
    plt.show()


    #Inverse Fourier of Img1 with Lpf
    G_lowpass = np.fft.ifftshift(Gshift_lowpass)
    g_lowpass = np.abs(np.fft.ifft2(G_lowpass))

    plt.imshow(g_lowpass, cmap='gray')
    plt.axis('off')
    plt.show()

    #Inverse Fourier of Img2 with Hpf
    G_highpass = np.fft.ifftshift(Gshift_highpass)
    g_highpass = np.abs(np.fft.ifft2(G_highpass))

    plt.imshow(g_highpass, cmap='gray')
    plt.axis('off')
    plt.show()
    combined_spectrum = (Gshift_lowpass + Gshift_highpass) / 2

    hybrid_spectrum = np.fft.ifftshift(combined_spectrum)
    hybrid_image = np.abs(np.fft.ifft2(hybrid_spectrum))

    plt.imshow(hybrid_image, cmap='gray')
    plt.axis('off')
    plt.show()
"""
# Display results in a 4x4 grid
    plt.figure(figsize=(12, 12))

    plt.subplot(4, 4, 1)
    plt.imshow(img01[:,:,::-1])  
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(4, 4, 2)
    plt.imshow(img02[:,:,::-1])  
    plt.title('Image 2')
    plt.axis('off')

    plt.subplot(4, 4, 3)
    plt.imshow(H_lowpass, cmap='gray')
    plt.title('Rectangular Lowpass Filter')
    plt.axis('off')

    plt.subplot(4, 4, 4)
    plt.imshow(H_highpass, cmap='gray')
    plt.title('Rectangular Highpass Filter')
    plt.axis('off')

    plt.subplot(4, 4, 5)
    plt.imshow(np.log1p(np.abs(Fshift1)), cmap='gray')
    plt.title('Fourier of Image 1')
    plt.axis('off')

    plt.subplot(4, 4, 6)
    plt.imshow(np.log1p(np.abs(Fshift2)), cmap='gray')
    plt.title('Fourier of Image 2')
    plt.axis('off')



    plt.subplot(4, 4, 7)
    plt.imshow(np.log1p(np.abs(Gshift_lowpass)), cmap='gray')
    plt.title('Filtered Fourier Image 1 (Lowpass)')
    plt.axis('off')

    plt.subplot(4, 4, 8)
    plt.imshow(np.log1p(np.abs(Gshift_highpass)), cmap='gray')
    plt.title('Filtered Fourier Image 2 (Highpass)')
    plt.axis('off')

    plt.subplot(4, 4, 9)
    plt.imshow(g_lowpass, cmap='gray')
    plt.title('Inverse LPF with Image 1')
    plt.axis('off')

    plt.subplot(4, 4, 10)
    plt.imshow(g_highpass, cmap='gray')
    plt.title('Inverse HPF with Image 2')
    plt.axis('off')

    plt.subplot(4, 4, 11)
    plt.imshow(hybrid_image, cmap='gray')
    plt.title('Combined Hybrid Image')
    plt.axis('off')

    plt.show()"""
# Test
#hybrid("/Users/akashpaijwar/Downloads/download.jpeg", "/Users/akashpaijwar/Downloads/download (1).jpeg")


