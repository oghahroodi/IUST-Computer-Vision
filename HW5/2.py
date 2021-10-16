# Ref: http://alyssaq.github.io/2014/understanding-hough-transform/


def hough_transform_line(image):
    img = image.copy()
    ro, theta = 0, 0

    # Step 1
    img = cv2.Canny(img, 50, 200, 3)

    # Step 2
    thetas = np.deg2rad(np.arange(-90.0, 90.0))
    w, h = img.shape
    max_ro = int(np.ceil(w * w + h * h))

    ros = np.linspace(-max_ro, max_ro, max_ro * 2.0)
    cos = np.cos(thetas)
    sin = np.sin(thetas)

    # Step 3
    accumulator = np.zeros((2 * max_ro, len(thetas)), dtype=np.uint64)
    y, x = np.nonzero(img)

    # Step 4
    for i in range(len(x)):
        for j in range(len(thetas)):
            ro = int(round(x[i] * cos[j] + y[i] * sin[j]) + max_ro)
            accumulator[ro, j] += 1
    i = np.argmax(accumulator)
    ro = ros[int(round(i / accumulator.shape[1]))]
    theta = thetas[int(round(i % accumulator.shape[1]))]
    return ro, theta, accumulator

