import os
import numpy as np
from PIL import Image
import pprint as pp

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '

# True je gscale1
moreLevels = True

def getAverageL(image):
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)

    # get shape
    w, h = im.shape

    # get average
    return np.average(im.reshape(w * h))


# open image and convert to grayscale
source_image_name = "Neo.jpg"
source_image_path = os.getcwd() + "\\" + source_image_name
# PA = palettised 256 colors with Alpha channel, L = luminance (grayscale), RGB
image = Image.open(source_image_path).convert('L')

# store dimensions
W, H = image.size[0], image.size[1]
print(f"source image dimensions: {W} x {H} px" )

# set scale default as 0.43 which suits
# a Courier font
scale = 1
cols = 200

# compute width of tile
w = W / cols

# compute tile height based on aspect ratio and scale
h = w / scale

# compute number of rows
rows = int(H / h)

print(f"columns: {cols}, rows: {rows}")
print(f"tile dimensions: {w} x {h}")

# check if image size is too small
if cols > W or rows > H:
    print("Image too small for specified cols!")
    exit(0)

# ascii image is a list of character strings
aimg = []

# generate list of dimensions
for j in range(rows):
    y1 = int(j * h)
    y2 = int((j + 1) * h)

    # correct last tile
    if j == rows - 1:
        y2 = H

    # append an empty string
    aimg.append("")

    for i in range(cols):

        # crop image to tile
        x1 = int(i * w)
        x2 = int((i + 1) * w)

        # correct last tile
        if i == cols - 1:
            x2 = W

        # crop image to extract tile
        img = image.crop((x1, y1, x2, y2))

        # get average luminance
        avg = int(getAverageL(img))

        # look up ascii char
        if moreLevels:
            gsval = gscale1[int((avg * 69) / 255)]
        else:
            gsval = gscale2[int((avg * 9) / 255)]

        # append ascii char to string
        aimg[j] += gsval

pp.pprint(aimg)
# image.show()