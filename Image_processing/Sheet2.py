# This package allows us to read and write images.
import imageio

# This package provides arrays for image data.
import numpy as np

# Here we define the file to read.
infile = "coffee-100.png"
# We now create a filename to write to based on the input.
outfile = infile[:-4] + ".sepia" + infile[-4:]

# Read the image file into an array.
img = imageio.imread(infile)

# Create a new array to hold the sepia image.  It has the
# same shape as the original image.
sepia = np.zeros(img.shape, dtype=np.uint8)
# Iterate over the image rows.
for x in range(0, img.shape[0]):
    # Iterate over the columns within a row.
    for y in range(0, img.shape[1]):
        # Save the red, green and blue values for this pixel.
        r = img[x][y][0]
        g = img[x][y][1]
        b = img[x][y][2]

        # Calculate the red channel sepia value for this pixel
        # capping it at 255 (which is the maximum value any
        # pixel can take).
        sepia[x][y][0] = min(round(0.393 * r + 0.769 * g + 0.189 * b), 255)
        # Calculate the green channel sepia value for this
        # pixel.
        sepia[x][y][1] = min(round(0.349 * r + 0.686 * g + 0.168 * b), 255)
        # Calculate the blue channel sepia value for this
        # pixel.
        sepia[x][y][2] = min(round(0.272 * r + 0.534 * g + 0.131 * b), 255)

        # Check whether there is a fourth channel (alpha).
        if img.shape[2] > 3:
            # Set the alpha channel to fully opaque.
            sepia[x][y][3] = img[x][y][3]

# Write out the final sepia image.
imageio.imwrite(outfile, sepia)
