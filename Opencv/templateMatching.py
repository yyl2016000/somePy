import cv2
import numpy as np

tpl = cv2.imread("D:/test/002.png")
target = cv2.imread("D:/test/001.png")

th, tw = tpl.shape[:2]
result = cv2.matchTemplate(target, tpl, cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

tl = max_loc

br = (tl[0]+tw, tl[0]+th)
cv2.rectangle(target, tl, br, (0, 0, 255), 2)
cv2.namedWindow("match", cv2.WINDOW_NORMAL)
cv2.imshow("match", target)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
