from PIL import Image
import random
from bisect import bisect
import os

greyscale = [
		" ",
		" ",
		".,-",
		"_ivc=!/|\\~",
		"gjez2]/(YL)t[+T7Vf",
		"mdK4ZGbNDXY5P*Q",
		"W8KMA",
		"#%$"
		]
path='' #give source path here.
dest='' #give destinationo paht here.
colourdepth=[36,72,108,144,180,216,252]
def make_thumbnail(image):
	im=Image.open(image)
	xvalue=im.size[0]
	yvalue=im.size[1]
	if xvalue>160:
		xnewvalue=160
		ynewvalue=yvalue/(xvalue/xnewvalue)
		im=im.resize((xnewvalue,ynewvalue),Image.BILINEAR)
	im=im.convert("L")
	return im
def make_ascii(image):
	str=''
	im=make_thumbnail(image)
	for y in range(0,im.size[1]):
		for x in range(0,im.size[0]):
			lum=255-im.getpixel((x,y))
			row=bisect(colourdepth,lum)
			possibles=greyscale[row]
			str=str+possibles[random.randint(0,len(possibles)-1)]+' '
		str=str+"\n"
	return str
for image in os.listdir(path):
	print image
	if image.endswith('.jpg'):
		f=open(dest+image.replace('.jpg',''),'w')
	if image.endswith('.JPG'):
		f=open(dest+image.replace('.JPG',''),'w')
	asciiart=make_ascii(path+image)
	f.write(asciiart)
