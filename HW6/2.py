def get_circles(image):
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100)
 

    if circles is not None:

        circles = np.round(circles[0, :]).astype("int")
        for x, y, r in circles:
            cv2.circle(img, (x, y), r, (255, 0, 0), 4)
            cv2.rectangle(img, (x - 3, y - 3), (x + 3, y + 3), (255, 0, 0), -1)

    return img

