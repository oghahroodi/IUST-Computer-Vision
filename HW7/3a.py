img_path = 'img.jpg'

import cv2
import dlib
import cv2
from imutils import face_utils

def get_facial_landmarks(image):
    img = image.copy()

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

    for (x, y) in shape:
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

    return img

