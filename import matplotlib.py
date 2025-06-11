import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('tob.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()