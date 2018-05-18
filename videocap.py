# -*- coding: utf-8 -*-

import sys
import datetime
import os
import cv2

def picture(img):
    #Make a 'picure' directroy when there is not
    if not os.path.exists('.\\picture'):
            os.makedirs('.\\picture')

    file = ".\\picture\\"
    d = datetime.datetime.today()
    name = file+'%s-%s-%s-%s-%s-%s'%(d.year, d.month, d.day, d.hour, d.minute, d.second)+'.png'
    #Save img
    cv2.imwrite(name,img)

def getWebCamera(): 
    args = sys.argv
    if (len(args)==2):
        return cv2.VideoCapture(int(args[1]))
    else:
        return cv2.VideoCapture(0)

def keyEvent(key,img):
    #Press 'S'key and Save img
    if key is ord("s"):
        picture(img)

def faceJudge():
    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #Get the WebCamera 
    cap = getWebCamera()

    #main loop
    while True:
        #Read WebCamera
        _, img = cap.read()
        if img is None:
            print("WebCamera could not be found")
            break

        #Make a gray img
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Face detection
        faces = face_cascade.detectMultiScale(img_gray, 1.1, 3)
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        print(f'fases = {len(faces): 4d}', end='\r')
        cv2.imshow("Faces judge", img)

        key = cv2.waitKey(5)
        keyEvent(key,img)
        #Press 'Q'key and end
        if key is ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    faceJudge()
