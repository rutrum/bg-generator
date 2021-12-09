from PIL import Image
import noise
import numpy as np
import random
import math

def main():
    HEIGHT = 1080
    WIDTH = 1920
    SIZEX = 50
    SIZEY = 75
    OFFSET = 60 
    base_color = init_color()
    base_color = [200, 50, 50]

    img = np.zeros([HEIGHT,WIDTH,3],dtype=np.uint8)
    for yi, y in enumerate(range(0, HEIGHT, SIZEY)):
        for xi, x in enumerate(range(-SIZEX, WIDTH, SIZEX)):
            rand = random_color(base_color)
            if yi % 2 == 0:
                img[max(0, y):y+SIZEY, max(0, x):x+SIZEX] = rand
            else:
                img[y:y+SIZEY, max(0, x+OFFSET):x+SIZEX+OFFSET] = rand

    print(base_color)
    add_noise(img)
    #perlin_noise(img)
    #draw_box(base_color, HEIGHT, WIDTH, img)
    save_image(img, "background.png")

def add_noise(img):
    w, h, _ = img.shape
    for x in range(w):
        for y in range(h):
            if random.randint(0, 100) < 50:
                img[x,y] = np.subtract(img[x,y], 10)

def perlin_noise(img):
    w, h, _ = img.shape
    for x in range(w):
        for y in range(h):
            n = noise.pnoise2(x/10, 
                            y/10, 
                            octaves=6, 
                            persistence=.7, 
                            lacunarity=1.7, 
                            base=0)
            img[x, y] = np.subtract(img[x,y], 20*(n+1))

def draw_box(base_color, HEIGHT, WIDTH, img):
    diameter = 500
    border = 10
    border_color = np.subtract(255, base_color)
    center = (int((HEIGHT-diameter)/2), int((WIDTH-diameter)/2))
    for y in range(center[0] - border, center[0] + diameter + border):
        for x in range(center[1] - border, center[1] + diameter + border):
            img[y,x] = border_color
    for y in range(center[0], center[0] + diameter):
        for x in range(center[1], center[1] + diameter):
            img[y,x] = base_color


def init_color():
    return [
        random.randint(25, 225),
        random.randint(25, 225),
        random.randint(25, 225),
    ]

def random_color(color):
    return list(map(lambda x:
        random.randint(
            int(math.pow(color[x], .98)), 
            int(min(math.pow(color[x], 1.02), 255)),
        ), [0, 1, 2]))

def save_image(nparray, name):
    im = Image.fromarray(nparray)
    im.save(name)

if __name__ == "__main__":
    main()
