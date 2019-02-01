def main():
    file = open("img.ppm", "w")
    head(file)
    body(file)

def head(file):
    file.write("P3 500 500 255")

num0 = 200
num1 = 100
num2 = 75
num3 = 150
#map = [[0] * m for i in range(n)]

def body(file):
    image=" "
    r=0
    g=0
    b=255
    i=0
    while i<500:
        ii=0
        g=0
        while ii<500:
            image += str(r) + " " + str(g) + " " + str(b) + " "
            ii+=1
            g=(ii*255)/500
        r=(i*255)/500
        i+=1
    file.write(image)

def draw():
    image=" "
    for i in map:
        image+=str(map[i][0]) + " " + str(map[i][1]) + " " + str(map[i][2]) + " "
    file.write(image)

main()
