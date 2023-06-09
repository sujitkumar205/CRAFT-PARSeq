# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture(os.getcwd() + "/Videos/1.MOV")
dest = os.getcwd() + "/CRAFT/TestImages/"

try:
    
    # creating a folder named data
    if not os.path.exists(dest):
        os.makedirs(dest)

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0

while(True):
    
    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = dest + '/frame' + str(currentframe) + '.jpeg'
        #print ('Creating...' + name)

        # writing the extracted images
        #frame = cv2.resize(frame, (0,0), fx=0.20, fy=0.20) 
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
