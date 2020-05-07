#!/usr/bin/env python3
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    r'/home/antonis/Desktop/Python/multi-proc/images/image-processing/image1.jpg',
    r'/home/antonis/Desktop/Python/multi-proc/images/image-processing/image2.jpg',
    r'/home/antonis/Desktop/Python/multi-proc/images/image-processing/image3.jpg',
    r'/home/antonis/Desktop/Python/multi-proc/images/image-processing/image4.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save('processed/{}'.format(img_name))
    print('{} was processed...'.format(img_name))


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print('Finished in {} seconds'.format(t2-t1))
