import os
collection = "CropWords/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("CropWords/" + filename, "CropWords/" + str(i) + ".jpg")