# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:15:43 2019

@author: Amisha Garg
"""
from PIL import Image

fname=input("enter file name")
img=Image.open(fname + str(".jpg"))
img_rotate = img.transpose(Image.ROTATE_90)
img_convert=img_rotate.convert(mode='L')
w=img_rotate.width/2
print(w)
h=img_rotate.height/2
img_crop=img_convert.crop(box=(w,h,160,204)).save("sample1.jpg")
img_thumb=img_convert.thumbnail((75,75))



    