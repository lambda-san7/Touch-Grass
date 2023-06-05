########################
# IMPORTS
########################

import pygame
from assets import (
    dir_path,
    window,
    text,
    running,
    fps,
    clock,
    grass,
    center,
    button,
    favicon
)

########################
# DEFAULT SHIT
########################

pygame.display.set_caption("Grass")
pygame.display.set_icon(favicon)
clicks = 0
color = (255,255,255)

########################
# SCENES
########################

scene = None

class game:
    def handle():
        global clicks
        global color
        window.fill((50,50,50))
        if clicks == 1:
            msg = text(32,f"You Have Touched {clicks} Time",thicc=2)
        if clicks != 1:
            msg = text(32,f"You Have Touched {clicks} Times",thicc=2)
        msg.render(10,10)
        window.blit(grass,(center.x(200),center.y(200)))
        MyButton = button("Touch The Grass!",32,color)
        if MyButton.hover(center.x(MyButton.txt.w),center.y(MyButton.txt.h)):
            MyButton = button("Now Click!",32,color)
        if MyButton.click(center.x(MyButton.txt.w),center.y(MyButton.txt.h)):
            clicks += 1
            print(color)
            color = list(color)
            if color[0] == 5:
                if color[1] == 255:
                    color[2] += 10
                    return
                color[1] += 10
                return
            if color[2] != 5:
                color[2] -= 10
                return
            if color[1] != 5:
                color[1] -= 10
                return
            if color[0] != 5:
                color[0] -= 10
                return    
            color = tuple(color)
        MyButton.render(center.x(MyButton.txt.w),center.y(MyButton.txt.h))

########################
# GAME LOOP
########################

scene = game

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit