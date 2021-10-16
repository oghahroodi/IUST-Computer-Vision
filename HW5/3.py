def get_lines(image):
    img = image.copy()

    edges = cv2.Canny(img, 50, 200, 3) 

    lines = cv2.HoughLines(edges,1 ,np.pi/180, 90)
    # print(lines.shape)
    for i in lines:
        for r, theta in i:
            x1, y1, x2, y2 = pol_to_car(r, theta)
            cv2.line(img,(x1,y1), (x2,y2), (255,0,0),2)
    return img

