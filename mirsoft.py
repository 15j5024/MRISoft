# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from TemplateMatch import TempMatch
from capture import capture

def mainloop():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # Width
    cap.set(4, 720)  # Height
    winHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    winWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    haiS = ["m1","m2","m3","m4","m5","m6","m7","m8","m9","p1","p2","p3","p4","p5","p6","p7","p8","p9",
    "s1","s2","s3","s4","s5","s6","s7","s8","s9","jt","jn","js","jp","jhk","jht","jch"]
    f = "./hai/reduce/"
    e = "_h.jpg"

    hai_img = []
    for h in haiS:
        hai_img.append(cv2.imread(f+h+e))

    while True:
        _, img = cap.read()
        if img is None: break

        for h in hai_img:
            TempMatch(img, h)

        cv2.imshow('img',img)
        key = cv2.waitKey(10)
        if key is ord('e'): break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == '__main__':
    mainloop()
