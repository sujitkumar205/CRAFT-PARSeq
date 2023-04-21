import torch
from PIL import Image
from strhub.data.module import SceneTextDataModule

import os
from os import listdir
from os.path import isfile, join

mypath = os.getcwd() + "/CropWords/"
onlyfiles = ["CropWords/"+f for f in listdir(mypath) if isfile(join(mypath, f))]

# Load model and image transforms
parseq = torch.hub.load('baudm/parseq', 'parseq', pretrained=True).eval()
img_transform = SceneTextDataModule.get_transform(parseq.hparams.img_size)

for i in onlyfiles:
	img = Image.open(i).convert('RGB')
	# Preprocess. Model expects a batch of images with shape: (B, C, H, W)
	img = img_transform(img).unsqueeze(0)

	logits = parseq(img)
	logits.shape  # torch.Size([1, 26, 95]), 94 characters + [EOS] symbol

	# Greedy decoding
	pred = logits.softmax(-1)
	label, confidence = parseq.tokenizer.decode(pred)
	print('Word in ' + i + ' is = {}'.format(label[0]))