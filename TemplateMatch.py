# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from nichika import nichika

f = "./hai/nichika/"
e = "_h_2.jpg"

img_nichi = cv2.imread(f + "hai04" + e)
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#img_gray = nichika(img_rgb)
template_nichi = cv2.imread(f + "p2" + e)
h, w = template_nichi.shape[:2]

res = cv2.matchTemplate(img_nichi,template_nichi,cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_nichi, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite("dst.jpg",img_nichi)
cv2.imshow("res", img_nichi)
cv2.waitKey(0)
cv2.destroyAllWindows()