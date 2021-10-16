def change_img(image, angle):
    c = np.array(image.shape)[1]/2, np.array(image.shape)[0]/2 
#     print(c)
    rotate = cv2.getRotationMatrix2D(c, angle, 1.0)
    return cv2.warpAffine(image, rotate, image.shape[1::-1], flags=cv2.INTER_LINEAR)


def detect_template(image, template):
    img = image.copy()
    for i in range(360):
        _, w, h = template.shape[::-1]
        template = change_img(template, i)
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        ans = np.where(res>=0.6)
        for j in zip(*ans[::-1]):
            cv2.rectangle(img, j, (j[0] + w, j[1] + h), (0,0,255), 2)
    return img


