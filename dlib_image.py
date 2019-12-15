# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:26:40 2019

@author: Bharath
"""
import cv2
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from align import AlignDlib
import dlib
from model import create_model
from datetime import datetime
import os

alignment = AlignDlib('shape_predictor_68_face_landmarks.dat')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('weights/nn4.small2.v1.h5')

cap = cv2.VideoCapture(0)

threshold = float(0.25)

def distance(emb1, emb2):
    return np.sum(np.square(emb1 - emb2))


embeddeds = np.zeros((128,1))

my_data =np.genfromtxt('embeddeds.csv',delimiter=',')



while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        bb = dlib.rectangle(int(x),int(y),(x+w),int(y+h))
        img_aligned = alignment.align(96, img, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)
        

        img_aligned = (img_aligned / 255.).astype(np.float32)
        temp = nn4_small2_pretrained.predict(np.expand_dims(img_aligned, axis=0))[0]
        # temp=temp[:,np.newaxis]
        
        # if len(embeddeds[0])==1:
        #     embeddeds=np.append(embeddeds, temp,1)
        # else:
        #     for i in range(len(embeddeds[0])):
        #         if i!=0:
        #             if distance(temp,embeddeds[:,i])>threshold:
        #                 embeddeds=np.append(embeddeds, temp,1)
        
        find = False
        
        for i in range(len(my_data[0])):
            d = distance(temp,my_data[:,i])
            if d<threshold:
                find = True
                break
            else:
                find = False
        
        if find:
            cv2.putText(img, 'Known Person', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            print('Known Person')
            
        else:
            cv2.putText(img, 'Unknown Person', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            print('Unknown Person')
            
            
    # if a==20:
    #     print('stranger identified')
    #     now = datetime.now()
    #     current_time = now.strftime("%H:%M:%S")
    #     fn = current_time+'.jpg'
    #     cv2.imwrite(os.path.join('unknown/',fn), img)
        
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    

cap.release()
cv2.destroyAllWindows()
