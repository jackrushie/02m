from PIL import Image, ImageFilter

#import pictures
img = Image.open('.\images\pik.jpg')

# add  BLUR effect to image
filtered_img = img.filter(ImageFilter.BLUR)
# Change format (RGB is colour)
grey_image = img.convert('L')
# Rotate
#roate_image = img.rotate(90)

# save images
filtered_img.save(".\images\pik_blur.png", 'png')
grey_image.save(".\images\pik_grey.png", 'png')

# Show images (open the file)
# grey_image.show()


# Note: save as PNG for options to work

# Print options available for PIL
# print(dir(img))

# more info on https://pillow.readthedocs.io/en/stable/
