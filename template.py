import math

filename = "picture.ppm"
Xres = 510
Yres = 510
Max_Color = 255

header = "P3 %d %d %d\n" % (Xres, Yres, Max_Color)

image_value = []
for i in range(Xres):
    temp = []
    for j in range(Yres):
        r = math.hypot(Xres - i, j)
        g = 0  # math.hypot(i, j)
        b = math.hypot(i, Yres - j)
        temp.append([r, g, b])
    image_value.append(temp)
    
f = open(filename, "w")
f.write(header)
for i in range(Xres):
    filler = ""
    for j in range(Yres):
        filler += str(int(image_value[i][j][0] % Max_Color)) + "\t"
        filler += str(int(image_value[i][j][1] % Max_Color)) + "\t"
        filler += str(int(image_value[i][j][2] % Max_Color)) + "\t"
    f.write(filler + "\n")
f.close()
