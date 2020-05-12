import sys
import os
from PIL import Image

# grab args
# images/
# images/new
folder = str(sys.argv[1])
new_folder = str(sys.argv[2])

# check path exists and create output folder
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through files in dir and convert to PNG
for filename in os.listdir(folder):
    if filename.endswith((".jpg")):
        img = Image.open(f'./{folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f"{new_folder}/{clean_name}.png", 'png')
