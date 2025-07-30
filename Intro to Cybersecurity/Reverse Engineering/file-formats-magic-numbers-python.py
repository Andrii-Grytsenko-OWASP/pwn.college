import sys

image_file = 'image.cimg'

image_header = b"<MAG"

f = open(image_file, 'wb')
f.write(image_header)
f.close()
