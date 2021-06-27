import cv2 as cv
from numpy import array

def generate_array(image_path :str) -> array:
    image = cv.imread(image_path,0)
    if image is None:
        #Raise exception if could not open file
        raise OSError(strerror="Could not open file from provided path.", filename=image_path)
    else:
        return image