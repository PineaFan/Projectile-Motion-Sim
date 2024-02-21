#Mostly messing around with Pygame
import math
import pygame
from ColourBank import Colour

pygame.init()

#Variables and functions:
angleText = pygame.font.SysFont('helvetica', 25)
normalText = pygame.font.SysFont('helvetica', 15)
running = True
lastX = 0
lastY = 0
lastAngle = 0
pulling = False
totalVelocity = 0
circleRadius = 200
oldRadius = circleRadius
lastTotalVelocity = 0

#Base shapes and screen setup
screen = pygame.display.set_mode([1000, 600])
pygame.draw.circle(screen,(Colour().white),(0,600),circleRadius)
pygame.draw.circle(screen,(Colour().black),(0,600),circleRadius - 2)


#Event loop
while running:

    #Allows quiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Angle line
    x,y = pygame.mouse.get_pos()
    if x - lastX > 2 or x -lastX < -2 and x != 0:
        angle = math.atan((600 - y)/x)

        #Draws line only to the circle edge
        newX = 0 + (circleRadius * math.cos(math.atan((600 - y)/x))) - 2
        newY = 600 - (circleRadius * math.sin(math.atan((600 - y)/x))) + 2
        pygame.draw.circle(screen,(Colour().black),(0,600),oldRadius)
        pygame.draw.circle(screen,(Colour().white),(0,600),circleRadius)
        pygame.draw.circle(screen,(Colour().black),(0,600),circleRadius - 2)
        pygame.draw.line(screen,(Colour().white),(0,600),(newX,newY),4)
        oldRadius = circleRadius

        #Adds angle text
        angle = angle * 180 / math.pi
        angle = math.floor(angle)
        textSurface = angleText.render(str(lastAngle),False,Colour().black)
        screen.blit(textSurface, (lastX * 1.05, lastY * 1.05 -60))

        textSurface = angleText.render(str(angle),False,Colour().white)
        screen.blit(textSurface, (newX * 1.05, newY * 1.05 - 60 ))
        
        lastX = newX
        lastY = newY
        lastAngle = angle

    #Velocity input based on pull and circle resizing
    if pygame.mouse.get_pressed(num_buttons = 3) == (True,False,False) and pulling is False:
        startX, startY = pygame.mouse.get_pos()
        pulling = True

    elif pygame.mouse.get_pressed(num_buttons = 3) == (True,False,False) and pulling is True:
        endX, endY = pygame.mouse.get_pos()
        xMovement = startX - endX
        yMovement = startY - endY
        totalVelocity = math.sqrt((xMovement**2) + (yMovement**2))
        circleRadius = 200 / ((totalVelocity/200) + 1)

        #Adds text
        textSurface = normalText.render(str(f"Input Velocity: {lastTotalVelocity}"),False,Colour().black)
        screen.blit(textSurface, (0,0))

        textSurface = normalText.render(str(f"Input Velocity: {totalVelocity}"),False,Colour().white)
        screen.blit(textSurface, (0,0))
        lastTotalVelocity = totalVelocity

    elif pygame.mouse.get_pressed(num_buttons = 3) == (False,False,False) and pulling is True:
        circleRadius = 200
        pulling = False

    pygame.display.flip()

pygame.quit()
