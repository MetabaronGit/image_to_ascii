import os
from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = '@%#*+=-:. '

# open image and convert to grayscale
source_image_name = "Neo.jpg"
source_image_path = os.getcwd() + "\\" + source_image_name
# PA = palettised 256 colors with Alpha channel, L = luminance (grayscale), RGB
image = Image.open(source_image_path).convert('L')

# store dimensions
W, H = image.size[0], image.size[1]
print(f"source image dimensions: {W} x {H} px" )

# image.show()