# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:38:51 2021

@author: Kylo Ren
"""
# Libraries
import cv2
import numpy as np
import pandas as pd
from tkinter import*
#img_dir=['rgb','gif','pbm','pgm','ppm','tiff','rast','xbm','jpeg','jpg','bmp','png','webp','exr']

#command functions

def view_image():
    link=link_entry.get()
    link_entry.delete(0,END)
    try:
        img=cv2.imread(link)
        cv2.imshow('Image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        link_entry.insert(0,'No link/file location found')
        
    
    
def view_video():
    link=link_entry.get()
    link_entry.delete(0,END)
    try:
        assert link[-3:]=='mp4'
        video=cv2.VideoCapture(link)
        while True:
            ret,frame=video.read()
            if ret==False:
                break
            cv2.imshow('Video',frame)
            cv2.waitKey(25)
        video.release()
        cv2.destroyAllWindows()
    except:
        link_entry.insert(0,'No link/file location found')
    
    
def quit_app():
    root.destroy()
    

# Build app

root = Tk()
root.title( 'RGB Studio' )
root.geometry( '700x200' )


## Link entrybox
heading=Label(root,text=""" Welcome to RGB STUDIO""")
link_label = Label(root,text='●● Enter the image link / location --->')
link_entry = Entry(root,width=70)
kyet_label = Label(root,text='Developed by s_agnik1511 with ❤️')


## Buttons 
image_viewer = Button(root,text='View Image',height=5,width=20,command=view_image)
video_viewer = Button(root,text='View Video',height=5,width=20,command=view_video)
quit_button=Button(root,text='QUIT',height=5,width=20,command=quit_app)

## Designing

link_label.place(x = 10 , y = 30)
link_entry.place(x = 220 , y = 30)
heading.place(x=350,y=5)
image_viewer.place(x=155,y=90)
video_viewer.place(x=325,y=90)
quit_button.place(x=495,y=90)
kyet_label.place(x=300,y=50)


root.mainloop()