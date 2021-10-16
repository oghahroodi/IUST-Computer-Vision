MAX_KERNEL_LENGTH = 3
from scipy.ndimage.filters import convolve



def gaussian_filter(image):
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        img = cv2.GaussianBlur(image, (i, i), 0)
    return img
 
def sobel(img):
    img = np.array(img, dtype=float)

    img = gaussian_filter(img)

    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    Ix = convolve(img,Gx) 
    Iy = convolve(img,Gy)


    grad = np.hypot(Ix, Iy)
    direction = np.arctan2(Iy, Ix)
    direction = (np.round(direction * (5.0 / np.pi)) + 5) % 5

    return img, grad, direction

def non_max_suppression(img, grad, direction):

    grad_copy = grad.copy()

    for i in range(len(img)):
        for j in range(len(img[i])):
            
            if i == 0 or i == len(img)-1 or j == 0 or j == len(img[i])-1:
                grad_copy[i, j] = 0
                continue
            d = direction[i, j] % 4
        
            if d == 0:
                if grad[i,j] <= grad[i,j-1] or grad[i,j] <= grad[i,j+1]:
                    grad_copy[i,j] = 0
            if d == 1:
                if grad[i,j] <= grad[i-1,j+1] or grad[i,j] <= grad[i+1,j-1]:
                    grad_copy[i, j] = 0
            if d == 2:
                if grad[i,j] <= grad[i-1,j] or grad[i,j] <= grad[i+1,j]:
                    grad_copy[i,j] = 0
            if d == 3:
                if grad[i,j] <= grad[i-1,j-1] or grad[i,j] <= grad[i+1,j+1]:
                    grad_copy[i,j] = 0
    return img, grad_copy


def threshold(img, grad_copy, th1, th2):

    edges = np.array((grad_copy > th2))
    all_posible_edges = edges + (grad_copy > th1)

    
    ans = edges.copy()
    p = []
    for i in range(1, len(img)-1):
        for j in range(1, len(img[i])-1):	
            if all_posible_edges[i,j] != 1:
                continue 


            patch = all_posible_edges[i-1:i+2,j-1:j+2]
            if patch.max() == 2:
                p.append((i,j))
                ans[i,j] = 1

    while len(p) > 0:
        p2 = []
        for i, j in p:
            for k in range(-1, 2):
                for w in range(-1, 2):
                    if k == 0 and w == 0: 
                        continue
                    tmp1 = i+k
                    tmp2 = j+w
                    if edges[tmp1, tmp2] == 1 and ans[tmp1, tmp2] == 0:
                        newPix.append((tmp1, tmp2))
                        ans[tmp1,tmp2] = 1
        p = p2

    return ans

def your_canny(image, th1, th2):
    img = image.copy()
    # step 1
    img = gaussian_filter(img)
    # step 2
    img, grad, direction = sobel(img)
    # step 3
    img, grad_copy = non_max_suppression(img, grad, direction)
    # step 4
    img = threshold(img, grad_copy,th1,th2)

    return img


def cv2_canny(image, th1, th2):
    img = image.copy()
    img = cv2.Canny(img,th1,th2)
    return img