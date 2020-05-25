import numpy as np
import cv2 
import pyautogui

img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
img = cv2.resize(img,dsize=(640,640),interpolation=cv2.INTER_CUBIC)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()