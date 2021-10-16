def otsu(img):
    img2 = img.copy()
    res = img.shape[0]*img.shape[1]
    mean = 1.0/res
    histogeram, _ = np.histogram(img, np.array(range(0, 256)))
    max_var = -10000
   
    for i in range(1,255):
        left = np.sum(histogeram[:i])*mean
        right = np.sum(histogeram[i:])*mean

        left_mean = np.mean(histogeram[:i])
        right_mean = np.mean(histogeram[i:])

        var = left*right*(left_mean-right_mean)**2

        if var > max_var:
            th = i
            max_var = var
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i][j]>=th):
                img2[i][j] = 255
            else:
                img2[i][j] = 0

    return img2

def otsu_image(image, local_area = 1):
    img = image.copy()
    if local_area==1:
        return otsu(img)
    else:

        img1 = otsu(img[0:len(image)//2,0:len(img[0])//2])
        img2 = otsu(img[0:len(image)//2,len(img[0])//2:])
        img3 = otsu(img[len(image)//2:,0:len(img[0])//2])
        img4 = otsu(img[len(image)//2:,len(img[0])//2:])

        tmp1 = np.concatenate((img1,img3),axis=0)
        tmp2 = np.concatenate((img2,img4),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)

        return img

def adaptive_threshold(image, block_size, c):
    img = image.copy()
    th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY ,block_size, c)
    return th

c_list = [2,4,6,8,10]
block_size_list = [5,7,9,11,13]
best_c = 5
best_block_size = 11

