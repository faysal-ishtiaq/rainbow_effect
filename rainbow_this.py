__author__ = 'firabby'

from PIL import Image
from PIL import ImageEnhance

file_path = str(input("Enter file (image) name : "))

input_image = Image.open(file_path)

img_height = input_image.size[1]

img_width = input_image.size[0]

input_image = input_image.convert("RGB")

filter_image = Image.new("RGB", [img_height, img_width], (255, 255, 255, 255))

height_break = []
for num in range(0, img_height, int(img_height/6)):
    height_break.append(num)

height_break.append(height_break[5]+int(img_height/6))

color_codes = [(255, 0, 0, 0), (255, 50, 0, 0), (255, 255, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (75, 0, 130, 0)]

pixels = filter_image.load()

for i in range(0, 6):
    for j in range(img_width):
        for k in range(height_break[i], height_break[i+1]):
            pixels[k, j] = color_codes[i]
            
filter_image.rotate(270)

enhancer = ImageEnhance.Color(input_image)

input_image = enhancer.enhance(0.50)
 
enhancer = ImageEnhance.Brightness(input_image)

input_image = enhancer.enhance(1.4)

new_image = Image.blend(input_image, filter_image, 0.5)

new_image.show()

new_image.save('output.jpg')
