import random
from PIL import Image,ImageDraw
import os

items = open("magicitems.txt","r").readlines()

itemList = [line.rstrip('\n') for line in items]
#nft number and iterator
x = 1

while x <= 100:
    #item number and interator
    i = 1
    nftlist = []

    while i <= 8:
        #creating random number to use for index of items
        rngInt = random.randint(1,len(itemList)-1)
        nftlist.append(itemList[rngInt])
        i += 1

    #cleaning up list into readable format
    nftString = "\n".join(nftlist)

    #creating background
    img = Image.new('RGB', (300,300), color=(0,0,0))
    

    d = ImageDraw.Draw(img)
    #adding items and nft number to image
    d.text((10,50), nftString, fill=(255,255,255))
    d.text((250,30), "#" + str(x) , fill=(255,255,255))
    
    try:
        img.save("nfts/nft" + str(x) + ".png")
    except:
        os.mkdir("nfts")
        img.save("nfts/nft" + str(x) + ".png")
    
    x += 1
