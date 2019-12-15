# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:01:58 2019

@author: Bharath
"""


import cv2
import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from align import AlignDlib
import dlib
from model import create_model
import os

alignment = AlignDlib('shape_predictor_68_face_landmarks.dat')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

nn4_small2_pretrained = create_model()
nn4_small2_pretrained.load_weights('weights/nn4.small2.v1.h5')


def distance(emb1, emb2):
    return np.sum(np.square(emb1 - emb2))


embeddeds = np.zeros((128,1))

for filename in os.listdir('employees'):
    print(filename)
    img_path = 'employees/'+filename
    img = cv2.imread(img_path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    for (x, y, w, h) in faces:
        print(filename)
        bb = dlib.rectangle(int(x),int(y),(x+w),int(y+h))
        img_aligned = alignment.align(96, img, bb, landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)

        img_aligned = (img_aligned / 255.).astype(np.float32)
        temp = nn4_small2_pretrained.predict(np.expand_dims(img_aligned, axis=0))[0]
        temp=temp[:,np.newaxis]
        
        embeddeds=np.append(embeddeds, temp,1)

embeddeds = embeddeds[:,1:]
print(embeddeds.shape)
np.savetxt('embeddeds.csv',embeddeds,delimiter=",")