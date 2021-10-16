# HomeWork 1
# DeadLine : 12:00 PM 12 Mehr 1398
# Total points : 100 pts
import cv2
import matplotlib.pyplot as plt
import os

# PART 4
# Implement this function so that calculate histogram from image.
# And show it with DrawHist helper function.
# Point : 35 pts


def CalcHist(ImagePath):
    hist = [0] * 256
    image = cv2.imread(ImagePath, 0)
    for i in image:
        for j in i:
            hist[j] += 1
    return hist


def DrawHist(hist):
    plt.stem(hist, use_line_collection=True)
    plt.show()


# Now Run Functions
hist = CalcHist(os.path.join('..', 'images', 'gray.jpg'))
DrawHist(hist)
