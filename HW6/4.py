import math

def get_res_val(image):
    img = image.copy()
    val = 0
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     for i in range(1, 11, 2):
#         a = cv2.GaussianBlur(img, (i, i), 0)

#     dst = cv2.Canny(a, 5, 100, None, 3)

#     cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    
#     lines = cv2.HoughLines(dst, 1, np.pi / 180, 10, None, 0, 0)
#     pts1 = []
#     pts2 = []

#     if lines is not None:
#         for i in range(0, len(lines)):
#             rho = lines[i][0][0]
#             theta = lines[i][0][1]
#             a = math.cos(theta)
#             b = math.sin(theta)
#             x0 = a * rho
#             y0 = b * rho
#             pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
#             pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
#             if (abs(pt2[0]-pt1[0])<30):
#                 pts1.append(pt1[0])
#                 pts2.append(pt2[0])
#                 cv2.line(img, pt1, pt2, (255,0,0), 1, cv2.LINE_AA)

#     pts1.sort()
#     pts2.sort()
#     for i in range(len(pts1)):
#         k = 1
#         while True:
#             if i+1<len(pts1):
#                 if pts1[i+1]<pts1[i]+11*k:
#                     del pts1[i+1]
#                     k+=1
#                 else:
#                     break
#             else:
#                 break
                
#     print(pts1)          
#     print(cdst.shape)
#     for i in range(len(pts1)):
#         if i+1<len(pts1):
# #             q = img[:,pts1[i]:pts1[i+1],:]
# #             print(q)

#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     cv2.circle(img, (335,70),2,(255,255,255))
#     cv2.circle(img, (375,70),2,(255,255,255))
#     cv2.circle(img, (415,70),2,(255,255,255))
    
    color = {161:0, 178:1, 230:2, 
             230:3, 233:4, 0:5, 
             133:6, 208:7,(204,204,204):8,
             255:9}

    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    x1 = 320
    x2 = 360
    x3 = 400
    x4 = 440
    y1 = 40
    y2 = 80

    histogram_array1 = np.zeros(256, np.int32)
    for i in range(y1, y2):
        for j in range(x1, x2):
#             print(img[i][j])
            intensity = img[i][j][0]
            histogram_array1[intensity] += 1
            
    histogram_array2 = np.zeros(256, np.int32)
    for i in range(y1, y2):
        for j in range(x2, x3):
#             print(img[i][j])
            intensity = img[i][j][0]
            histogram_array2[intensity] += 1
            
    histogram_array3 = np.zeros(256, np.int32)
    for i in range(y1, y2):
        for j in range(x3, x4):
#             print(img[i][j])
            intensity = img[i][j][0]
            histogram_array3[intensity] += 1
        
    c1 = max(histogram_array1)
    c2 = max(histogram_array2)
    c3 = max(histogram_array3)
    print(c1,c2,c3)
    print(color[c1])
    print(color[c2])
    print(color[c3])
#     plt.plot(histogram_array1)
#     plt.show()
            

#     print(color)
#     n1 = 0
#     n2 = 0
#     n3 = 0
#     for i in color.keys():
#         if (abs(p1_c1[0]-i[0])<100 and abs(p1_c1[1]-i[1])<100 and abs(p1_c1[2]-i[2])<100):
#             n1 = color[i]
#         if (abs(p2_c1[0]-i[0])<100 and abs(p2_c1[1]-i[1])<100 and abs(p2_c1[2]-i[2])<100):
#             n2 = color[i]
#         if (abs(p3_c1[0]-i[0])<100 and abs(p3_c1[1]-i[1])<100 and abs(p3_c1[2]-i[2])<100):
#             print(color[i])
#             n3 = color[i]
#     print(n1)
#     print(n2)
#     print(n3)
    
#     val = (n1*10+n2) * 10**n3
#     print(val)

#     plt.imshow(img)

    
    return val

