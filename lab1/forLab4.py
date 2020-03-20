from PIL import Image, ImageFont, ImageDraw
import numpy as np

image = Image.fromarray(np.zeros((100, 100))+170)
draw = ImageDraw.Draw(image)

# use a bitmap font
font = ImageFont.truetype("arial.ttf", 150)

draw.text((0, 0), "o", font=font)
image.show()