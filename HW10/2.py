import imutils
from scipy.spatial import distance as dist
from collections import OrderedDict
import matplotlib.pyplot as plt

class ShapeDetector:
    def __init__(self):
        pass
 
    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        return shape


def detect_shape(image):
    img = image.copy()
    shape = []
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    for c in cnts:
        shape.append(sd.detect(c))
    return shape, cnts

def get_num_conneted(image):
    img = image.copy()
    number_of_connected = 0
    return number_of_connected

def get_num_holes(image):
    img = image.copy()
    number_of_holes = 0
    return number_of_holes

def get_num_obj_holes(image):
    img = image.copy()
    number_of_obj_holes = 0
    return number_of_obj_holes

def get_num_squares(image):
    img = image.copy()
    shape,_ = detect_shape(img)
    number_of_squares = 0
    for i in shape:
        if (i == 'square' or i == 'rectangle'):
            number_of_squares+=1
    return number_of_squares

def get_num_circles(image):
    img = image.copy()
    number_of_circles = 0
    shape,_ = detect_shape(img)
    number_of_squares = 0
    for i in shape:
        if (i == 'circle' or i == 'pentagon'):
            number_of_circles+=1
    return number_of_circles

