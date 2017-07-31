import python.darknet
import os, sys

net = python.darknet.load_net("cfg/yolo-caddy.cfg", "backup/yolo-caddy_40000.weights")
meta = python.darknet.load_meta("cfg/caddy.data")

folder = sys.argv[1]
files = os.listdir(folder)

for f in files:
    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
        print f
        path = os.path.join(folder, f)
        im = python.darknet.load_img(path)
        res = python.darknet.detector(net, meta, im)
        
        for i in range(meta.classes):
            xmin = res[i].xmin
            ymin = res[i].ymin
            xmax = res[i].xmax
            ymax = res[i].ymax
            if xmin != 0 or ymin != 0 or xmax != 0 or ymax != 0:
                print meta.names[res[i].index] + " " + str(xmin) + " " + str(ymin) + " " + str(xmax) + " " + str(ymax)
        python.darknet.free(net)
