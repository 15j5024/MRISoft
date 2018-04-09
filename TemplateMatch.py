# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
from nichika import nichika

def TempMatch(img_src, template):

    #画像読み込み
    #img_dst = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)
    img_dst = nichika(img_src)
    w, h = template.shape[::-1]

    #テンプレートマッチ
    res = cv2.matchTemplate(img_dst,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_dst, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    return img_dst

if __name__ == '__main__':

    hai = ["m1","m2","m3","m4","m5","m6","m7","m8","m9","p1","p2","p3","p4","p5","p6","p7","p8","p9",
    "s1","s2","s3","s4","s5","s6","s7","s8","s9","jt","jn","js","jp","jhk","jht","jch"]

    bace = "hai04"
    f1 = "./hai/reduce/"
    f2 = "./hai/dst/nichi/" + bace + "/"
    e1 = "_h.jpg"
    e2 = "_h_dst.jpg"
    bace = f1 + bace +e1

    for i in hai:
        name1 = f1 + i + e1
        name2 = f2 + i + e2

        # 画像の読み込み
        template = cv2.imread(name1, 0)
        img_bace = cv2.imread(bace)
        #マッチング
        img_dst = TempMatch(img_bace, template)
        
        cv2.imwrite(name2,img_dst)
        #cv2.imshow("res", img_nichi)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

