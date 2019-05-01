# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:29:40 2019

@author: MRS
"""

from PIL import Image, ImageDraw
import random



#Our square colors:
#red, yellow, green,dark_green, blue, dark_blue,
# orange, dark_purple, dark_yellow, turquoise, violet
myColors = ["#DA0000", "#FFEC04","#10FF01","#088500","#0BEAF8",
            "#F9BA05","#AF05F9","#B7B917","#F905EE","#F4AFFC"]

#File that saves the centres of the squares
f = open("centres2.txt", 'w')

def create_image(imageName):
    image = Image.new('RGB', (128, 128), 'black') 

    draw = ImageDraw.Draw(image)
    
   

    #print 10 squaeres per image in random positions
    for k in range(0,10):
        
        x0 = random.randint(0, 118)
        y0 = random.randint(0, 118)
        
        draw.rectangle((x0, y0, x0+10, y0+10), fill=myColors[k], outline=myColors[k]) 
        #draw.point((x0+5, y0+5), fill = 'white')
        #write centres
        f.write(str(x0+5) + " " + str(y0+5))
        f.write('\n')
        
        image.save(imageName)
        

#create 1000 images:
        
for i in range(0,1000):
     
    imageName = r"C:\Users\MRS\Documents\Belen\ucm\4.5\GCOM\images\ " + str(i) + "square.jpg"
    create_image(imageName)

f.close