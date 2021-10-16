def get_skeleton(image):
    img = image.copy()
    skeleton = img.copy()
    skeleton[:,:] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    while True:
        erosion = cv2.erode(img, kernel, iterations = 1)
        dilation = cv2.dilate(erosion, kernel, iterations = 1)
        tmp  = cv2.subtract(img, dilation)
        skeleton = cv2.bitwise_or(skeleton, tmp)
        img[:,:] = erosion[:,:]
        if cv2.countNonZero(img) == 0:
            break
    return skeleton

