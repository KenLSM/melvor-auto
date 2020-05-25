import numpy as np
import cv2
import pyautogui

# For some reason the height and width is scaled up by 2x
# might be due to display scaling
WINDOW_WIDTH = 1680 * 2 // 2
WINDOW_HEIGHT = 945 * 2


def capture_img():
    "Captures screen region and returns img"
    img = pyautogui.screenshot(region=(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img


def downscale_img(img, n):
    "Down scales image by n"
    DOWN_WIDTH = WINDOW_WIDTH // n
    DOWN_HEIGHT = WINDOW_HEIGHT // n
    img = cv2.resize(img, dsize=(DOWN_WIDTH, DOWN_HEIGHT),
                     interpolation=cv2.INTER_CUBIC)
    return img


def mark(arr, i, ii):
    "Insert and stores tuples of interest into array"
    arr.append([i, ii])


def join_points():
    "Receives an array of tuples and forms unions of connected tuples"
    pass


# Locate orange bar 149, 133, 123
# for i in [0, 1]:
def mark_pixels(img, pixels_to_match):
    "Locate matching pixels and returns the array of matched points"
    arr = []
    for i in range(img.shape[1]):
        interest = img[:, i]
        line_len = len(interest)
        # print(interest)
        for ii in range(line_len):
            if (interest[ii] == pixels_to_match).all():
                # print('found', ii, i)
                mark(arr, i, ii)

    return arr


# try find runite
# print(DOWN_WIDTH, DOWN_HEIGHT)
# interest = img[:, 187]
# print(interest)

img = capture_img()
img = downscale_img(img, 8)

orange_bar_mark_rev = [149, 133, 123][::-1]

points = mark_pixels(img, orange_bar_mark_rev)

print(points)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
