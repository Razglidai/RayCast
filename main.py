import math
import sys
import time

import pygame
raySpeed = 0.01
deph = 100
# Map = ['#################################################','#...............................................#','#...#...........................................#','#...................#...........................#','#...................#...........................#','#......##...........#...........................#','#...............................................#','#...............................................#','#################################################',]
Map = pygame.PixelArray(pygame.image.load('1.png'))
MapW = 689
MapH = 559
class Player:
    PosX = 100.0
    PosY = 100.0
    PlAngel = 0.0
    PlVision = 90.0
    PlSpeed = 100

    def forward(self):
        x_ang = math.cos(math.radians(self.PlAngel))
        y_ang = math.sin(math.radians(self.PlAngel))
        self.PosX = self.PosX + self.PlSpeed * x_ang
        self.PosY = self.PosY + self.PlSpeed * y_ang

    def backward(self):
        x_ang = math.cos(math.radians(self.PlAngel))
        y_ang = math.sin(math.radians(self.PlAngel))
        self.PosX = self.PosX - self.PlSpeed * x_ang
        self.PosY = self.PosY - self.PlSpeed * y_ang

    def TurnRight(self):
        self.PlAngel = self.PlAngel +  15

    def TurnLeft(self):
        self.PlAngel = self.PlAngel - 15

    def myPos(self):
        print(self.PosX,self.PosY,self.PlAngel)

class point:
    x:int
    y:int
    Map: pygame.PixelArray

    def __init__(self, x, y,Map:pygame.PixelArray):
        self.x = x
        self.y = y
        self.Map = Map
        self.Map[self.x,self.y] = pygame.Color(0,255,0)
    def  __del__(self):
        self.Map[self.x,self.y] = pygame.Color(0,0,0)



class Screen:
    player: Player
    ScW = 1260
    ScH = 720
    pygame.display.init()

    surf = pygame.display.set_mode(size=(ScW, ScH), display=0)
    pixelArray = pygame.PixelArray(surf)
    hWall = 600

    ColorGrass = pygame.Color(127, 255, 0)
    ColorSky = pygame.Color(135, 206, 235)





    def ObjectLong(self,pixelAngel: float):
        x = self.player.PosX
        y = self.player.PosY
        RayHit = False
        dist = 0
        x_ang  = math.cos(math.radians(pixelAngel))
        y_ang = math.sin(math.radians(pixelAngel))
        while not RayHit and  dist < deph:
            dist += raySpeed
            x += dist * x_ang
            y += dist * y_ang
            if x < 0 or y < 0 or y > MapH or x > MapW:
                RayHit = True
                break
            if Map[int(x),int(y)] == pygame.Color(255, 255, 255):
                RayHit = True
                break
        return dist



    def setScreen(self):

        for j in range(self.ScW):
                Angel = self.player.PlAngel - self.player.PlVision / 2 + j * self.player.PlVision / self.ScW
                wallong = self.ObjectLong(Angel) * math.cos(math.radians(Angel - self.player.PlAngel))

                wObject = self.hWall / wallong
                color = pygame.Color(100, 100, 100)
                for i in range(self.ScH):
                    if i > (self.ScH / 2 - wObject/2) and i < (self.ScH / 2 + wObject/2):
                            self.pixelArray[j, i] = color
                    elif i > (self.ScH / 2 + wObject/2):
                        self.pixelArray[j, i] = self.ColorGrass
                    elif i < (self.ScH / 2 - wObject/2):
                        self.pixelArray[j, i] = self.ColorSky
                    elif i == (self.ScH / 2 - wObject/2):
                        self.pixelArray[j, i] = pygame.Color(0, 0, 0)
                    elif i == (self.ScH / 2 + wObject/2):
                        self.pixelArray[j, i] = pygame.Color(0, 0, 0)




screen = Screen()
player = Player()
screen.player = player
Time = time.time()
while True:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
               player.forward()
            if event.key == pygame.K_s:
               player.backward()
            if event.key == pygame.K_d:
               player.TurnRight()
            if event.key == pygame.K_a:
               player.TurnLeft()
            if event.key == pygame.K_g:
               player.myPos()

    screen.setScreen()
    pygame.display.update()
