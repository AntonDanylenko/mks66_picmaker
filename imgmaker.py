import random

def main():
    file = open("img.ppm", "w")
    head(file)
    body(file)

def head(file):
    file.write("P3 500 500 255")

map = [[[0] * 3 for i in range(500)]for i in range(500)]

def body(file):
    image=" "
    r=127
    g=127
    b=127
    i=0
    while i<500:
        ii=0
        g=127
        while ii<500:
            if i==0:
                g=127
            else:
                g = map[i][ii-1][1] + random.randint(random.randint(-5,-1),random.randint(1,7))
            if g<0:
                g=0
            elif g>255:
                g=255
            if i==0:
                b=127
            else:
                b = map[i][ii-1][2] + random.randint(random.randint(-5,-1),random.randint(1,7))
            if b<0:
                b=0
            elif b>255:
                b=255
            map[i][ii][0] = r
            map[i][ii][1] = g
            map[i][ii][2] = b
            ii+=1
        i+=1
    draw(file)

def draw(file):
    image=" "
    i=0
    while i<500:
        ii=0
        while ii<500:
            #print(str(map[i][ii][0]) + " " + str(map[i][ii][1]) + " " + str(map[i][ii][2]) + " ")
            image+=str(map[i][ii][0]) + " " + str(map[i][ii][1]) + " " + str(map[i][ii][2]) + " "
            ii+=1
        i+=1
    file.write(image)

main()
