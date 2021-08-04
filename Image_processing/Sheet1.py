import imageio

infile = "/Users/njk77/Documents/CS_sutton_cam/img/balloon-100.jpg"
img = imageio.imread(infile)

# print info about image
print("Type: ", type(img))
print("Shape: ", img.shape)
print("Data type: ", img.dtype)

import numpy as np
print("R: ", img[0][0][0])
print("G: ", img[81][99][1])
print("B: ", img[40][49][2])
print("RGB: ", img[19][74])

newimg1 = np.zeros((100, 200, 3), dtype = np.uint8)
print("New img 1 shape: ", newimg1.shape)

newimg2 = np.zeros(img.shape, dtype = np.uint8)
print("New img 2 shape : ", newimg2.shape)