img_path = 'Q2-img.jpeg'

import math
import matplotlib.pyplot as plt

def get_four_lines(image):
    img = image.copy()
    img2 = image.copy()
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img, 3, 60, 60)
    img = cv2.medianBlur(img, 7)

    edges = cv2.Canny(img, 200, 300)
#     plt.imshow(edges)
    
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    h = len(edges)
    w = len(edges[0])
    area = (w - 10) * (h - 10)
    area_found = area * 0.5
    contour = np.array([[1, 1], [1, h-1], [w-1, h-1], [w-1, 1]])

    for i in contours:
        perimeter = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.03 * perimeter, True)
        if (len(approx) == 4 and cv2.isContourConvex(approx) and area_found < cv2.contourArea(approx) < area):
            area_found = cv2.contourArea(approx)
            contour = approx

    cv2.line(img2, (contour[0][0][0],contour[0][0][1]), (contour[1][0][0],contour[1][0][1]), (255,0,0), 3)
    cv2.line(img2, (contour[1][0][0],contour[1][0][1]), (contour[2][0][0],contour[2][0][1]), (255,0,0), 3)
    cv2.line(img2, (contour[2][0][0],contour[2][0][1]), (contour[3][0][0],contour[3][0][1]), (255,0,0), 3)
    cv2.line(img2, (contour[3][0][0],contour[3][0][1]), (contour[0][0][0],contour[0][0][1]), (255,0,0), 3)
                
    return img2

