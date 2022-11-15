import math
import sys

import pygame
rayItr = 400
raySpeed = 0.01
deph = 20
Map = ['#################################################',
       '#...............................................#',
       '#.......#.......................................#',
       '#...............................................#',
       '#...............................................#',
       '#...............................................#',
       '#...............................................#',
       '#...............................................#',
       '#################################################',
       ]

class Player:
    PosX = 2.0
    PosY = 2.0
    PlAngel = 0.0
    PlVision = 90.0
    def forward(self):
        self.PosX += 1 * math.cos(math.radians(self.PlAngel))
        self.PosY += 1 * math.sin(math.radians(self.PlAngel))
    def backward(self):
        self.PosX -= 1 * math.cos(math.radians(self.PlAngel))
        self.PosY -= 1 * math.sin(math.radians(self.PlAngel))
    def TurnRight(self):
        self.PlAngel += 15
    def TurnLeft(self):
        self.PlAngel -= 15
    def myPos(self):
        print(self.PosX,self.PosY,self.PlAngel)


class Screen:
    player: Player
    ScW = 800
    ScH = 600
    ScD = 6
    pygame.display.init()

    surf = pygame.display.set_mode(size=(ScW, ScH), display=0)
    pixelArray = pygame.PixelArray(surf)
    hWall = 6

    def ObjectLong(self,pixelAngel: float):
        x = self.player.PosX
        y = self.player.PosY
        RayHit = False
        dist = 0
        x_ang  = math.sin(math.radians(pixelAngel))
        y_ang = math.cos(math.radians(pixelAngel))
        while not RayHit and  dist < deph:
            dist += raySpeed
            x += dist * x_ang
            y += dist * y_ang
            if x < 0 or y<0 or x >=deph + self.player.PosX or y >=deph + self.player.PosY:
                RayHit = True
                dist = deph
                break
            if Map[int(y)][int(x)] == '#':
                RayHit = True
                break
        return dist



    def setScreen(self):

        for j in range(self.ScW):
                Angel = self.player.PlAngel - self.player.PlVision / 2 + j * self.player.PlVision / self.ScW
                wallong = self.ObjectLong(Angel)
                wObject = self.ScD * self.hWall / wallong

                for i in range(self.ScH):
                    if i > (self.ScH / 2 - wObject/2) and i < (self.ScH / 2 + wObject/2):
                        if wallong > 15:
                            self.pixelArray[j, i] = pygame.Color(102, 102, 102)
                        elif wallong > 10:
                            self.pixelArray[j, i] = pygame.Color(153, 153, 153)
                        elif wallong > 5:
                            self.pixelArray[j, i] = pygame.Color(204, 204, 204)
                        elif wallong > 0:
                            self.pixelArray[j, i] = pygame.Color(255, 255, 255)




screen = Screen()
screen.player = Player()

while True:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            screen.player.forward()
        elif event.type == pygame.KEYDOWN:
            screen.player.backward()
        elif event.type == pygame.K_RIGHT:
            screen.player.TurnRight()
        elif event.type == pygame.K_LEFT:
            screen.player.TurnLeft()
        elif event.type == pygame.K_g:
            screen.player.myPos()
    screen.setScreen()
    pygame.display.update()

