#I think that all programs that are their own languages should have a main file.
#example: main.sh, main.py, main.js
import ai_vision
from PIL import Image
from PIL import ImageFilter

#open the subject image.
image = Image.open("subject.jpg")

#get the subject image's initial dimensions.
image_width = image.size[0]
image_height = image.size[1]

#save the subject as a grayscaled image.
#image = image.convert("L")
#image.save("grayscale_subject.jpg")

#open the subject image.
#image = Image.open("grayscale_subject.jpg")

#run gaussian blur over the grayscalled image.
#image = image.filter(ImageFilter.GaussianBlur(radius=2))
#image.save("blurred_subject.jpg")

image = image.filter(ImageFilter.FIND_EDGES)
image.save("edged_subject.jpg")

#loaded image object into memory.
pixels = image.load()
for y in range(image_height):
    for x in range(image_width):
        #pixelColor = img.getpixel((x, y)) #the slow method.
        pixel_color = pixels[x, y]
        print pixel_color