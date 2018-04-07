# -*- coding: utf-8 -*-
 
import numpy as np
import cv2
import sys

# usage
# > python 09-02_SIFT_matching.py
#      <INPUT_FILE1>     Doraemon6_1.jpg
#      <INPUT_FILE2>     Doraemon6_2.jpg

argvs = sys.argv
argc = len(argvs)

if (argc != 3):
  print('Usage: > python 09-02_SIFT_matching.py <INPUT_FILE1> <INPUT_FILE2>')
  quit()

INPUT_FILE1 = sys.argv[1]
INPUT_FILE2 = sys.argv[2]

# 画像の読み込み
img_src1 = cv2.imread(INPUT_FILE1, cv2.IMREAD_GRAYSCALE)
img_src2 = cv2.imread(INPUT_FILE2, cv2.IMREAD_GRAYSCALE)

# 特徴抽出器の作成
detector = cv2.xfeatures2d.SIFT_create()

# kptsは特徴点(keypoint)の位置, descは特徴ベクトル(128次元)
kpts1, desc1 = detector.detectAndCompute(img_src1, None)
kpts2, desc2 = detector.detectAndCompute(img_src2, None)

# 特徴点の比較
matcher = cv2.BFMatcher()
# desc2から最も近い2つを選ぶ
matches = matcher.knnMatch(desc1, desc2, k=2)

# データを間引きする
# 最も近い点が2番目に近い点の距離の0.6倍のものを保存
good = []
ratio = 0.6
for m,n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])

# 対応する特徴点同士を描画
img_dst = cv2.drawMatchesKnn(img_src1, kpts1, img_src2, kpts2, good, None, flags=2)

cv2.imwrite("SIFT_result.jpg", img_dst)
cv2.imshow('dst', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
