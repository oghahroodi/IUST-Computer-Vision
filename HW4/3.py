from matplotlib import pyplot as plt


def denoise_image(image):
    img = image.copy()
    ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    ftshift = np.fft.fftshift(ft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(ftshift[:, :, 0], ftshift[:, :, 1]))

    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum')
    plt.show()
    
    point1 = [60,90,120,145]
    point2 = [60,90,160,185]
    point3 = [170,190,140,160]
    point4 = [170,190,175,200]
    for i in range(point1[0],point1[1]):
        for j in range(point1[2],point1[3]):
            ftshift[i][j] = 0.001    
            
    for i in range(point2[0],point2[1]):
        for j in range(point2[2],point2[3]):
            ftshift[i][j] = 0.001    
            
    for i in range(point3[0],point3[1]):
        for j in range(point3[2],point3[3]):
            ftshift[i][j] = 0.001    
            
    for i in range(point4[0],point4[1]):
        for j in range(point4[2],point4[3]):
            ftshift[i][j] = 0.001


    inv_fshift = np.fft.ifftshift(ftshift)
    img_recon = cv2.idft(inv_fshift)
    img_recon = cv2.magnitude(img_recon[:, :, 0], img_recon[:, :, 1])

    ft = cv2.dft(np.float32(img_recon), flags=cv2.DFT_COMPLEX_OUTPUT)
    ftshift = np.fft.fftshift(ft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(ftshift[:, :, 0], ftshift[:, :, 1]))



    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum')
    plt.show()
            

 
    return img_recon



