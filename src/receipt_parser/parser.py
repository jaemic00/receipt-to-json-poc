
import pytesseract
import cv2 as cv

def parse_receipt(receipt_array):
    img_data = pytesseract.image_to_data(receipt_array, output_type=pytesseract.Output.DICT)
    img = None;
    n_boxes = len(img_data['level'])
    for i in range(n_boxes):
        (x,y,w,h) = (img_data['left'][i], img_data['top'][i], img_data['width'][i], img_data['height'][i])
        img = cv.rectangle(receipt_array, (x,y), (x + w, y + h), (0,0,255), 2)
    cv.imwrite("lool.jpg", img);
    pass