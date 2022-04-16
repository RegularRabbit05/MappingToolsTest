import struct
from PIL import Image

im = Image.open("treemap.png")   

trees = []

width, height = im.size
for x in range(width):
    for y in range(height):
        r,g,b = im.getpixel((x,y))
        if r > 128 and g > 128 and b > 128:
            trees.append([float(x),float(0.0),float(y)])

bytesMap = []

for t in trees:
    l1, l2, l3 = list(struct.pack("f", t[0])), list(struct.pack("f", t[1])), list(struct.pack("f", t[2]))
    bytesMap.append(l1[0])
    bytesMap.append(l1[1])
    bytesMap.append(l1[2])
    bytesMap.append(l1[3])
    bytesMap.append(l2[0])
    bytesMap.append(l2[1])
    bytesMap.append(l2[2])
    bytesMap.append(l2[3])
    bytesMap.append(l3[0])
    bytesMap.append(l3[1])
    bytesMap.append(l3[2])
    bytesMap.append(l3[3])

bytesFile = bytes(bytesMap)

with open("0.tma", "wb") as treeMapFile:
    treeMapFile.write(bytesFile)
