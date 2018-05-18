# -*- coding: utf-8 -*-
 
import cv2
import numpy as np
 
if __name__ == '__main__':

    hai = ["m1","m2","m3","m4","m5","m6","m7","m8","m9","p1","p2","p3","p4","p5","p6","p7","p8","p9",
    "s1","s2","s3","s4","s5","s6","s7","s8","s9","jt","jn","js","jp","jhk","jht","jch"]

    hai.extend(["hai01", "hai02", "hai03", "hai04"])

    f1 = "./hai/original/hai1/"
    f2 = "./hai/reduce2/"
    e1 = ".jpg"
    e2 = "_h.jpg"

    for i in hai:
        name1 = f1 + i + e1
        name2 = f2 + i + e2
        # 画像の読み込み
        img_src = cv2.imread(name1)
        #リサイズ(1/8)
        height, width= img_src.shape[:2]
        img_dst = cv2.resize(img_src,(round(width/8),round(height/8)))
        #保存
        cv2.imwrite(name2,img_dst)
        