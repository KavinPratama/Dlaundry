from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('tober.png')
plt.imshow(img)
plt.axis('off')
plt.show()