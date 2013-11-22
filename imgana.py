import os
from PIL import Image
import matplotlib.pyplot as plt


if not os.path.exists("result"):
    os.makedirs("result")


    
pics_dir = "pics"
filenames = os.listdir(pics_dir)

lr_all = [0] * 256
lg_all = [0] * 256
lb_all = [0] * 256

print "Begin"

for picname in filenames:
    print picname
    
    filename = os.path.join(pics_dir, picname)
    im = Image.open(filename)

    lr = [0] * 256
    lg = [0] * 256
    lb = [0] * 256
    
    w, h = im.size
    for i in range(w):
        for j in range(h):
            color = im.getpixel((i,j))
            lr[color[0]] += 1
            lg[color[1]] += 1
            lb[color[2]] += 1
            lr_all[color[0]] += 1
            lg_all[color[1]] += 1
            lb_all[color[2]] += 1
    """
    data = im.getdata()
    for color in data:
        lr[color[0]] += 1
        lg[color[1]] += 1
        lb[color[2]] += 1
        lr_all[color[0]] += 1
        lg_all[color[1]] += 1
        lb_all[color[2]] += 1
    """
        

    pr = [r*1.0/sum(lr) for r in lr]
    plt.title("R")
    plt.figure(figsize=(10,3))
    plt.xlim(0,256)
    #plt.ylim(0,1)
    plt.ylabel('R')
    left = tuple(range(256))
    height = tuple(pr)
    rect = plt.bar(left=left ,height=height,width=1,align="center")
    plt.savefig('r.jpg')
    plt.close('all')

    pg = [g*1.0/sum(lg) for g in lg]
    plt.title("G")
    plt.figure(figsize=(10,3))
    plt.xlim(0,256)
    #plt.ylim(0,1)
    plt.ylabel('G')
    left = tuple(range(256))
    height = tuple(pg)
    rect = plt.bar(left=left ,height=height,width=1,align="center")
    plt.savefig('g.jpg')
    plt.close('all')

    pb = [b*1.0/sum(lb) for b in lb]
    plt.title("B")
    plt.figure(figsize=(10,3))
    plt.xlim(0,256)
    #plt.ylim(0,1)
    plt.ylabel('B')
    left = tuple(range(256))
    height = tuple(pb)
    rect = plt.bar(left=left ,height=height,width=1,align="center")
    plt.savefig('b.jpg')
    plt.close('all')

    imr = Image.open("r.jpg")
    img = Image.open("g.jpg")
    imb = Image.open("b.jpg")

    ima = Image.new('RGB', (1000,900))
    ima.paste(imr, (0,0))
    ima.paste(img, (0,300))
    ima.paste(imb, (0,600))
    ima.save("result/" + picname.split(".")[0] + "_result.jpg")


pr = [r*1.0/sum(lr_all) for r in lr_all]
plt.title("R")
plt.figure(figsize=(10,3))
plt.xlim(0,256)
#plt.ylim(0,1)
plt.ylabel('R')
left = tuple(range(256))
height = tuple(pr)
rect = plt.bar(left=left ,height=height,width=1,align="center")
plt.savefig('r.jpg')
plt.close('all')

pg = [g*1.0/sum(lg_all) for g in lg_all]
plt.title("G")
plt.figure(figsize=(10,3))
plt.xlim(0,256)
#plt.ylim(0,1)
plt.ylabel('G')
left = tuple(range(256))
height = tuple(pg)
rect = plt.bar(left=left ,height=height,width=1,align="center")
plt.savefig('g.jpg')
plt.close('all')

pb = [b*1.0/sum(lb_all) for b in lb_all]
plt.title("B")
plt.figure(figsize=(10,3))
plt.xlim(0,256)
#plt.ylim(0,1)
plt.ylabel('B')
left = tuple(range(256))
height = tuple(pb)
rect = plt.bar(left=left ,height=height,width=1,align="center")
plt.savefig('b.jpg')
plt.close('all')

imr = Image.open("r.jpg")
img = Image.open("g.jpg")
imb = Image.open("b.jpg")

ima = Image.new('RGB', (1000,900))
ima.paste(imr, (0,0))
ima.paste(img, (0,300))
ima.paste(imb, (0,600))
ima.save("result/all_result.jpg")



raw_input("Finish!")





