import cv2
import numpy as np

img = cv2.imread('D:/001.jpg',0)
print(img)
cv2.imshow('theImage', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('D:/002.png',img)
    cv2.destroyAllWindows()