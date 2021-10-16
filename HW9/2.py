import cv2
import numpy as np
import math

import matplotlib.pyplot as plt

def get_num_circles(image):
    img = image.copy()
    number_of_circles = 0
#     for i in range(2,100):
#         kernel = np.ones((i,i),np.uint8)

#         e = cv2.erode(img ,kernel, iterations = 1)
#         ret, labels = cv2.connectedComponents(e)
#         if ret==22:
#             print(ret)
#             print(i)
#             print('------')
#             break

    
    kernel1 = np.ones((25,25),np.uint8)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,8))
    kernel2 = np.ones((13,8),np.uint8)
    e1 = cv2.erode(img ,kernel1, iterations = 1)
    e2 = cv2.erode(img ,kernel2, iterations = 1)

    if np.sum(e1) == 0:
        ret, labels = cv2.connectedComponents(e2)
#         print(ret)
        return ret-1
    else:
        ret, labels = cv2.connectedComponents(e1)
#         print(ret)
        return ret-1

    
   

bonus_part = True

def get_val_coins(image):
    img = image.copy()
    val_of_coins = 0
    kernel1 = np.ones((25,25),np.uint8)
    e1 = cv2.erode(img ,kernel1, iterations = 1)
    ret, labels = cv2.connectedComponents(e1)
    unique, counts = np.unique(labels, return_counts=True)
    money = dict(zip(unique, counts))
    small_c = 0
    big_c = 0
    for i in money:
        if i!=0:
#             print(money[i])
            if money[i]<1000:
                small_c+=1
            else:
                big_c+=1
        
    
    return small_c*100+big_c*500

