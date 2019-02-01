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
    r=0
    g=127
    b=255
    rise = 1
    x=0
    while x<500:
        rise += random.randint(-1,1)
        if rise<0:
            rise=0
        elif rise>10:
            rise=10
        increase = random.randint(-2,rise)
        y=0
        while y<500:
            if y==0:
                if x==0:
                    g = 127
                else:
                    g = map[x][y-1][1] + random.randint(-1,1)
            else:
                g = map[x-1][y][1] + increase
            print("g: " + str(g))
            if g<0:
                g=0
            elif g>255:
                g=255
            map[x][y][0] = r
            map[x][y][1] = g
            map[x][y][2] = b
            y+=1
        x+=1
    draw(file)

def draw(file):
    image=" "
    y=0
    while y<500:
        x=0
        while x<500:
            #print(str(map[i][ii][0]) + " " + str(map[i][ii][1]) + " " + str(map[i][ii][2]) + " ")
            image+=str(map[x][y][0]) + " " + str(map[x][y][1]) + " " + str(map[x][y][2]) + " "
            x+=1
        y+=1
    file.write(image)

main()
