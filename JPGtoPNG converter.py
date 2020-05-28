import sys
import os
from PIL import Image

# grab arguments
img_folder = sys.argv[1]
out_folder = sys.argv[2]

# check if new directory exists
if not os.path.exists(out_folder)
    os.makedirs(out_folder)

count=0
# loop thorugh folder
for filename in os.listdir(img_folder)
# convert images
    img - Image.open(f'{img_folder}{filename}')
    clean_name =os.path.splitext(filename)[0]
# save to new
    img.save(f'{out_folder{clean_name}', 'png')
    count+=0

print(f'Suscessfully converted {count} image(s)')