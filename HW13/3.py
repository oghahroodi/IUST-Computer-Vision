def face_cat_detector(image):
    img = image.copy()
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    rects = detector.detectMultiScale(gray, minNeighbors=5, minSize=(60, 60))
    # loop over the cat faces and draw a rectangle surrounding each
#     print(rects)
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    return img

