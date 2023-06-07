#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os,sys
from PIL import Image


size = 256, 256 #바꾸고 싶은 사이즈
path = "/Users/kim-yeoeun/Downloads/photo_yeoeun" #이미지 경로
modified_path = "/Users/kim-yeoeun/Downloads/y_photo" #resize된 이미지가 저장될 경로
os.chdir(path)



def resize_and_crop(img_path, modified_path, size, crop_type='middle'):
    
    files = os.listdir(img_path)
    
    for file in files: 
        
        name = str(file)
        os.chdir(img_path)
        img = Image.open(file)
        img_ratio = img.size[0] / float(img.size[1])
        ratio = size[0] / float(size[1])
   
    
        if ratio > img_ratio:
            img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
                Image.ANTIALIAS)     
            if crop_type == 'top':
                box = (0, 0, img.size[0], size[1])
            elif crop_type == 'middle':
                box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                    int(round((img.size[1] + size[1]) / 2)))
            elif crop_type == 'bottom':
                box = (0, img.size[1] - size[1], img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
            
        elif ratio < img_ratio:
            img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
                Image.ANTIALIAS)
            if crop_type == 'top':
                box = (0, 0, size[0], img.size[1])
            elif crop_type == 'middle':
                box = (int(round((img.size[0] - size[0]) / 2)), 0,
                    int(round((img.size[0] + size[0]) / 2)), img.size[1])
            elif crop_type == 'bottom':
                box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
            
        else :
            img = img.resize((size[0], size[1]), Image.ANTIALIAS)
            
        os.chdir(modified_path)
        img.save(name, "PNG")


resize_and_crop(path, modified_path, size)


# In[ ]:




