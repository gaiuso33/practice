import pydicom
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def fourier_transform(image):
    f = np.fft.fft2(image)    
    fshift = np.fft.fftshift(f)
    magnitude_spectrum=20*np.log(np.abs(fshift))
    return magnitude_spectrum


img1=pydicom.dcmread('C:/Users/Ayogaius/Desktop/IM000004.dcm').pixel_array
img2=pydicom.dcmread('C:/Users/Ayogaius/Desktop/IM000001.dcm').pixel_array


ft1= fourier_transform(img1)
ft2= fourier_transform(img2)

fig, ((ax1, ax2), (ax3, ax4))= plt.subplots(2,2, figsize=(12,12))

ax1.imshow(img1,cmap='gray')
ax1.set_title('Image 1')
ax1.axis('off')

ax2.imshow(img2,cmap='gray')
ax2.set_title('Image 2')
ax2.axis('off')

ax3.imshow(ft1,cmap='gray')
ax3.set_title('Fourier transform of Image 1')
ax3.axis('off')

ax4.imshow(ft2,cmap='gray')
ax4.set_title('Fourier Transform of Image 2')
ax4.axis('off')

plt.tight_layout()
plt.show()
