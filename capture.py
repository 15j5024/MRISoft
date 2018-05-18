# -*- coding: utf-8 -*-
import cv2
class capture():
    def __init__(self):
        self = cv2.VideoCapture(1)
        self.set(3, 1280)  # Width
        self.set(4, 720)  # Height
    def getHeight(self):
        return int(self.get(cv2.CAP_PROP_FRAME_HEIGHT))
    def getWidth(self):
        return int(self.get(cv2.CAP_PROP_FRAME_WIDTH))
