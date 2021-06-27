from numpy import array
import cv2 as cv
#Takes an image array reprezentation and uses Otsu binarization to enhance it. 
def enhance_receipt(image_array : array) -> array:
    return cv.threshold(image_array,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]