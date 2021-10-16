img_path = 'img.jpg'

import dlib
import imutils
import cv2 as cv
from imutils import face_utils
import math

def change_image(img, img_overlay, pos, alpha_mask):

    x,y = pos
    y1,y2 = max(0, y),min(img.shape[0], y+img_overlay.shape[0])
    x1,x2 = max(0, x),min(img.shape[1], x+img_overlay.shape[1])

    y1_eye,y2_eye = max(0,-y), min(img_overlay.shape[0], img.shape[0]-y)
    x1_eye,x2_eye = max(0,-x), min(img_overlay.shape[1], img.shape[1]-x)
    channels = img.shape[2]

    alpha = alpha_mask[y1_eye:y2_eye, x1_eye:x2_eye]
    alpha_inv = 1.0-alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha_inv*img_overlay[y1_eye:y2_eye, x1_eye:x2_eye, c]+alpha * img[y1:y2, x1:x2, c])


def get_added_reality_image(image):
    img = image.copy()
    
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    img2 = img.copy()

    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    boundary = detector(gray, 1)

    for (i, rect) in enumerate(boundary):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face_utils.rect_to_bb(rect)

#         for (x, y) in shape:
#             cv.circle(frame, (x, y), 2, (0, 0, 0), -1)

        x1 = shape[17][0]
        x2 = shape[26][0]
        y1 = shape[19][1]
        y2 = shape[28][1]
        g = cv.imread('g.jpg')

        g = cv2.resize(g, ((x2 - x1), (y2 - y1)))
        change_image(img2, g, (shape[17][0], shape[17][1]), g[:, :, 2] / 255.0)

    w = img.shape[1]
    h = img.shape[0]
    r = float(w)/float(h)
    hh = 900
    img = cv2.resize(img,(int(hh*r), hh))

    
    return img2

