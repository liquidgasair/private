import os
import numpy as np
import time
import pygame
from pygame import camera
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, Conv2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from io import BytesIO
from pyautogui import alert

time.sleep(1)
model= keras.models.load_model('E:/Programms2/cnn/models')

pygame.init()
camera.init()
win_w=640
win_h=480
display= pygame.display.set_mode((win_w,win_h),0)
framerate= pygame.time.Clock()
run=True

def predict():
    img=keras.preprocessing.image.load_img('./images/bottle.jpg', grayscale=False, color_mode="rgb", target_size=(100,100), interpolation="nearest")
    input_arr = keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])
    result=model.predict(input_arr)
    m= 0
    out= 0
    for i in result:
        for g in range(len(i)):
            if i[g]>m:
                m=i[g]
                out=g
        if out==0:
            return('AluCan')
        elif out==1:
            return('Glass')
        elif out==2:
            return('HDPEM')
        elif out==3:
            return('PET')
        else:
            return('Error')
        
size=(640,480)
camera = pygame.camera.Camera(pygame.camera.list_cameras()[0], size)
camera.start()
while run:
    framerate.tick(75)
    screen = pygame.surface.Surface(size, 0, display)
    screen = camera.get_image(screen)
    display.blit(pygame.transform.flip(screen,True, False), (0,0))
    pygame.display.update()
    if pygame.event.get(pygame.KEYDOWN):
        
        img = pygame.surface.Surface(size, 0, display)
        img = camera.get_image(img)
        pygame.image.save(img, 'master.jpg')
        time.sleep(1)
        result= predict()
        alert(text=result, title='', button='OK')
        
                    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:   
            run=False 
    