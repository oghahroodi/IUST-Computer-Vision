def get_hist(image):
    hist = [0] * 256
    for i in image:
        for j in i:
            hist[j] += 1
    return hist

def s_hist(image):
#     transform_functions = [[(color_s, color_d) for color_s, color_d in zip(range(256), range(256))] for _ in range(local_area)]
    h = get_hist(image)
    fmax = 0
    fmin = 255
    for i, count in enumerate(h):
        if count!=0:
            fmax = max(i, fmax)
            fmin = min(i, fmin)
    transform_functions = []
    t = {}
    for color, count in enumerate(h):
        if color>=fmin and color<=fmax:
            transform_functions.append((color, ((color-fmin)/(fmax-fmin)*255)))
            t[color] = ((color-fmin)/(fmax-fmin)*255)
        elif color<fmin:
            transform_functions.append((color, 0))
        elif color>fmax:
            transform_functions.append((color, 255))
            
    img = deepcopy(image)
    for i,row in enumerate(image):
        for j,color in enumerate(row):
            img[i][j] = t[image[i][j]]
#     print(fmin)
#     print(fmax)
            
#     print(image[50][50])
#     print(img[50][50])
                
    return img, transform_functions



def stretch_hist(image, local_area = 1):
    if local_area==1:
        img, tf = s_hist(image)
        transform_functions = [tf]
    elif local_area==4:
        
        img1, transform_functions1 = s_hist(image[0:len(image)//2,0:len(image[0])//2])
        img2, transform_functions2 = s_hist(image[0:len(image)//2,len(image[0])//2:])
        img3, transform_functions3 = s_hist(image[len(image)//2:,0:len(image[0])//2])
        img4, transform_functions4 = s_hist(image[len(image)//2:,len(image[0])//2:])
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4]

        tmp1 = np.concatenate((img1,img3),axis=0)
        tmp2 = np.concatenate((img2,img4),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)
    
    elif local_area==8:
        
        img1, transform_functions1 = s_hist(image[0:len(image)//4,0:len(image[0])//2])
        img2, transform_functions2 = s_hist(image[len(image)//4:2*len(image)//4,0:len(image[0])//2])
        img3, transform_functions3 = s_hist(image[2*len(image)//4:3*len(image)//4,0:len(image[0])//2])
        img4, transform_functions4 = s_hist(image[3*len(image)//4:,0:len(image[0])//2])
        img5, transform_functions5 = s_hist(image[0:len(image)//4,len(image[0])//2:])
        img6, transform_functions6 = s_hist(image[len(image)//4:2*len(image)//4,len(image[0])//2:])
        img7, transform_functions7 = s_hist(image[2*len(image)//4:3*len(image)//4,len(image[0])//2:])
        img8, transform_functions8 = s_hist(image[3*len(image)//4:,len(image[0])//2:])
        
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4,transform_functions5,transform_functions6,transform_functions7,transform_functions8]

        tmp1 = np.concatenate((img1,img2,img3,img4),axis=0)
        tmp2 = np.concatenate((img5,img6,img7,img8),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)

                
    return img, transform_functions


def c_hist(image):
#     transform_functions = [[(color_s, color_d) for color_s, color_d in zip(range(256), range(256))] for _ in range(local_area)]
    h = get_hist(image)
    fmax = 0
    fmin = 255
#     for i, count in enumerate(h):
#         if count!=0:
#             fmax = max(i, fmax)
#             fmin = min(i, fmin)
    percent = sum(h)//100
    s = 0
    for i in range(len(h)):
        s+=h[i]
        if s>= percent:
            fmin = i
            break
            
    s = 0
    for i in range(len(h)-1,-1,-1):
        s+=h[i]
        if s>= percent:
            fmax = i
            break
#     print(fmin)
#     print(fmax)
    transform_functions = []
    t = {}
    for color, count in enumerate(h):
        if color>=fmin and color<=fmax:
            transform_functions.append((color, ((color-fmin)/(fmax-fmin)*255)))
            t[color] = ((color-fmin)/(fmax-fmin)*255)
        elif color<fmin:
            transform_functions.append((color, 0))
        elif color>fmax:
            transform_functions.append((color, 255))
            
    img = deepcopy(image)
#     print(t)
    for i,row in enumerate(image):
        for j,color in enumerate(row):
            if image[i][j] in t.keys():
                img[i][j] = t[image[i][j]]
            
#     print(image[50][50])
#     print(img[50][50])
                
    return img, transform_functions



def clip1_hist(image, local_area = 1):
    if local_area==1:
        img, tf = c_hist(image)
        transform_functions = [tf]
    elif local_area==4:
        
        img1, transform_functions1 = c_hist(image[0:len(image)//2,0:len(image[0])//2])
        img2, transform_functions2 = c_hist(image[0:len(image)//2,len(image[0])//2:])
        img3, transform_functions3 = c_hist(image[len(image)//2:,0:len(image[0])//2])
        img4, transform_functions4 = c_hist(image[len(image)//2:,len(image[0])//2:])
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4]

        tmp1 = np.concatenate((img1,img3),axis=0)
        tmp2 = np.concatenate((img2,img4),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)
    
    elif local_area==8:
        
        img1, transform_functions1 = c_hist(image[0:len(image)//4,0:len(image[0])//2])
        img2, transform_functions2 = c_hist(image[len(image)//4:2*len(image)//4,0:len(image[0])//2])
        img3, transform_functions3 = c_hist(image[2*len(image)//4:3*len(image)//4,0:len(image[0])//2])
        img4, transform_functions4 = c_hist(image[3*len(image)//4:,0:len(image[0])//2])
        img5, transform_functions5 = c_hist(image[0:len(image)//4,len(image[0])//2:])
        img6, transform_functions6 = c_hist(image[len(image)//4:2*len(image)//4,len(image[0])//2:])
        img7, transform_functions7 = c_hist(image[2*len(image)//4:3*len(image)//4,len(image[0])//2:])
        img8, transform_functions8 = c_hist(image[3*len(image)//4:,len(image[0])//2:])
        
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4,transform_functions5,transform_functions6,transform_functions7,transform_functions8]

        tmp1 = np.concatenate((img1,img2,img3,img4),axis=0)
        tmp2 = np.concatenate((img5,img6,img7,img8),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)

                
    return img, transform_functions

def e_hist(image):

    h = get_hist(image)
    cdf = {}

    transform_functions = []
    t = {}
    s = 0
    for color, count in enumerate(h):
        s+=count
        t[color] = 255 * s / sum(h)
        transform_functions.append((color,255 * s / sum(h)))
    
            
    img = deepcopy(image)

    for i,row in enumerate(image):
        for j,color in enumerate(row):
            if image[i][j] in t.keys():
                img[i][j] = t[image[i][j]]
            

                
    return img, transform_functions



def equalize_hist(image, local_area = 1):
    if local_area==1:
        img, tf = e_hist(image)
        transform_functions = [tf]
    elif local_area==4:
        
        img1, transform_functions1 = e_hist(image[0:len(image)//2,0:len(image[0])//2])
        img2, transform_functions2 = e_hist(image[0:len(image)//2,len(image[0])//2:])
        img3, transform_functions3 = e_hist(image[len(image)//2:,0:len(image[0])//2])
        img4, transform_functions4 = e_hist(image[len(image)//2:,len(image[0])//2:])
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4]

        tmp1 = np.concatenate((img1,img3),axis=0)
        tmp2 = np.concatenate((img2,img4),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)
    
    elif local_area==8:
        
        img1, transform_functions1 = e_hist(image[0:len(image)//4,0:len(image[0])//2])
        img2, transform_functions2 = e_hist(image[len(image)//4:2*len(image)//4,0:len(image[0])//2])
        img3, transform_functions3 = e_hist(image[2*len(image)//4:3*len(image)//4,0:len(image[0])//2])
        img4, transform_functions4 = e_hist(image[3*len(image)//4:,0:len(image[0])//2])
        img5, transform_functions5 = e_hist(image[0:len(image)//4,len(image[0])//2:])
        img6, transform_functions6 = e_hist(image[len(image)//4:2*len(image)//4,len(image[0])//2:])
        img7, transform_functions7 = e_hist(image[2*len(image)//4:3*len(image)//4,len(image[0])//2:])
        img8, transform_functions8 = e_hist(image[3*len(image)//4:,len(image[0])//2:])
        
        transform_functions = [transform_functions1,transform_functions2,transform_functions3,transform_functions4,transform_functions5,transform_functions6,transform_functions7,transform_functions8]

        tmp1 = np.concatenate((img1,img2,img3,img4),axis=0)
        tmp2 = np.concatenate((img5,img6,img7,img8),axis=0)
        img = np.concatenate((tmp1,tmp2),axis=1)

                
    return img, transform_functions

