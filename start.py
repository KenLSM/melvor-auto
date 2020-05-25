import numpy as np
import cv2
import pyautogui
WINDOW_WIDTH = 1680 * 2 // 2
WINDOW_HEIGHT = 945 * 2
# 1680x945*2.00
print(pyautogui.size().width)
img = pyautogui.screenshot(region=(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

DOWN_WIDTH = WINDOW_WIDTH // 8
DOWN_HEIGHT = WINDOW_HEIGHT // 8
img = cv2.resize(img, dsize=(DOWN_WIDTH, DOWN_HEIGHT),
                 interpolation=cv2.INTER_CUBIC)


# print([149, 133, 123] == [149, 133, 123])
orange_bar_mark_rev = [149, 133, 123][::-1]
print(orange_bar_mark_rev)

arr = []


def mark(i, ii):
    arr.append([i, ii])


# Locate orange bar 149, 133, 123
# for i in [0, 1]:
for i in range(img.shape[1]):
    interest = img[:, i]
    line_len = len(interest)
    # print(interest)
    for ii in range(line_len):
        if (interest[ii] == orange_bar_mark_rev).all():
            print('found', ii, i)
            mark(i, ii)
            # raise Exception()
        # print(len(interest))
        # print(interest)


# try find runite
# print(DOWN_WIDTH, DOWN_HEIGHT)
# interest = img[:, 187]
# print(interest)


cv2.imshow('image', img)
# cv2.imshow('interest', img[:, 140:160])
# cv2.imshow('interest2', img[187, :])

cv2.waitKey(0)
cv2.destroyAllWindows()
