import os
import cv2
import numpy as np

def read_image(dir_image):
    image = cv2.imread(dir_image)
    return image

def resize_image(image, dim):
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return image

def crop_fit_circle_image(image):
    hh, ww = image.shape[:2]

    # define circles
    xc = hh // 2
    yc = ww // 2
    r  = hh // 2

    mask            = np.zeros_like(image)
    mask            = cv2.circle(mask, (xc,yc), xc, (255,255,255), -1)

    result          = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask[:,:,0]
    return result

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def get_name(dir_gallery):
    name = dir_gallery.split("/")[-1].replace("_20.jpg","")
    return name
