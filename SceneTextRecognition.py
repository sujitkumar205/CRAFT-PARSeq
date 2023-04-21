import os
from os import listdir
from os.path import isfile, join

mypath = os.getcwd() + "/CropWords/"
onlyfiles = ["CropWords/"+f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
	os.remove(i)

mypath = os.getcwd() + "/CRAFT/TestImages/"
onlyfiles = ["CRAFT/TestImages/"+f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
	os.remove(i)	

os.system("python VideoToFrames.py")
os.system("python CRAFT/pipeline.py --trained_model=CRAFT/craft_mlt_25k.pth --test_folder=CRAFT/TestImages")
os.system("python CRAFT/crop_images.py")
os.system("python renameImages.py")
os.system("python parseq/predict.py")