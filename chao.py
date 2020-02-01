#xn+1 - rxn(1-xn)
import matplotlib.pyplot as plt
import pygame
import numpy
from video import make_video
pygame.init()
width = int(500*(16/9))
height = 500
main_surface = pygame.display.set_mode((width,height))
save_screen = make_video(main_surface, "hehe")

arr = []
equ = []
rate= []
rae = 0


def solver(r, x, n, m):
    if n>0:
        arr.append((r*x*(1-x)))
        n-=1
        solver(r, (r*x*(1-x)), n, m)
    else:
        #print(arr)
        for s in range(100):
            equ.append(r+1)
            equ.append(arr[len(arr)-(s+1)])
        #print(equ)
        #plt.plot(arr)
        #plt.ylabel('some numbers')
        #plt.show()
def draw():
    f = 0
    scalex = ((max(equ[::2])-min(equ[::2])))
    scaley = ((max(equ[1::2])-min(equ[1::2])))
    maxx = max(equ[::2])
    maxy = max(equ[1::2])
          
    for val in range(len(equ)):
        ev = pygame.event.poll()
        if ((val+1)*2) < len(equ):
            x = (equ[val*2])
            y = (equ[(val*2)+1])
            x = int(((maxx-x)/scalex)*width)
            y = int(((maxy-y)/scaley)*height)

        if x>=(width) and f == 0:
            next(save_screen)
            main_surface.fill((0,0,0))
            arr.clear()
            equ.clear()
            rate.clear()
            f = 1
        pygame.draw.line(main_surface, (255,255,255), (x, y), (x, y), 1)
        pygame.display.flip()
        
for som in range(1):#range(1000):
    for x in range(200):
        #rae = 4-(1/(400))*(x)
        rae = 4-(4/(200))*(x)
        #rae = 4-(1/(20000))*(x)
        #solver(rae, 0.2, 100, 0.1+((1/200)*som))
        solver(rae, 0.4, 1000, 0)
    draw()


#plt.scatter(equ[::2],equ[1::2],  s = 0.1)


#plt.show()




    
    
