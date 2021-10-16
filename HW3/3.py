MAX_KERNEL_LENGTH = 7


def gaussian_filter(image):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv2.GaussianBlur(image, (i, i), 0)
    return img

def median_filter(image):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv2.medianBlur(image, i)
    return img


