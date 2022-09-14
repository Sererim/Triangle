from random import randint as rand
from turtle import *

hideturtle()
screensize(800, 600, "black")
shape("triangle")
def main():
    penup()
    #count = int(inpt("Enter amount of interation for generation of Serpinsky triangle.\n"))
    # (xa,ya) = (0,300) | (xb,yb) = (-400, -300) | (xc,yc) = (400, -300)
    count = 100000000
    xa , ya , xb , yb , xc , yc = 0.0 , 300.0 , -400.0, -300.0, 400.0, -300.0
    x = xa
    y = ya
    position = 0
    while count != 0:
        position = rand(0,2)
        if position == 0:
            x = (x+xa)/2
            y = (y+ya)/2
        if position == 1:
            x = (x+xb)/2
            y = (y+yb)/2
        if position == 2:
            x = (x+xc)/2
            y = (y+yc)/2
        setposition(x,y)
        dot(2,"white")
        count -= 1
        print(count)
    done()


if __name__ == '__main__':
    main()