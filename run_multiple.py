import os, sys
import os.path
import time

folder = "../Downloads/dataset3/image/"

images = os.listdir(folder)
images = [folder + image for image in images]

i = 0

for image in images:
    print image
    cmd = "./darknet detector test cfg/custom.data cfg/yolo_custom.cfg backup/75k.backup " + image
    os.system(cmd)
    
    if os.path.isfile("predictions.png"):
        os.rename("predictions.png", "multi/image_" + str(i) + ".png")
    elif os.path.isfile("predictions.jpg"):
        os.rename("predictions.jpg", "multi/image_" + str(i) + ".jpg")

    i += 1
    time.sleep(1)

