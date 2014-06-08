from pil import Image

def resize(imgFile):
	im1 = Image.open(imgFile)
	width, height = im1.size
	ratio = (width*100/height)
	#if ratio < 60 or ratio > 150:
	#	print imgFile
	#im1.close()
	print imgFile, "(original):", width, "x", height
	im2 = im1.resize((150,150), Image.ANTIALIAS)
	im2.save(imgFile)
	width, height = im2.size
	print imgFile, "(new):", width, "x", height

import os
for imgFile in os.listdir("."):
	if imgFile.endswith(".jpg") or imgFile.endswith(".png"):
		resize(imgFile)
