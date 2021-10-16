from copy import copy, deepcopy


def convert_level(image, src_level, dst_level):
    img = deepcopy(image)
    src_power = int(log2(src_level))
    dst_power = int(log2(dst_level))
    power = src_power - dst_power
#     print(power)
    for i in range(0,len(img)):
        for j in range(0, len(img[i])):
            img[i][j] = img[i][j] >> power
    return img

