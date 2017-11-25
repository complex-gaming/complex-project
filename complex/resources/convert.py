import os
from PIL import Image


image_folder = 'minimaps/'
output_folder = 'minimaps/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = [f for f in os.listdir(image_folder) if os.path.isfile(image_folder + f) and not f.startswith('.')]

for file in files:
    f, e = os.path.splitext(file)
    outfile = output_folder + f + ".png"
    Image.open(image_folder + file).save(outfile)


