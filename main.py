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
    button
)

########################
# DEFAULT SHIT
########################

pygame.display.set_caption("Stream")
#pygame.display.set_icon(favicon)
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
            msg = text(32,f"You Have Touched {clicks} Time")
        if clicks != 1:
            msg = text(32,f"You Have Touched {clicks} Times")
        msg.render(10,10)
        window.blit(grass,(center.x(200),center.y(200)))
        MyButton = button("Touch The Grass!",32,color)
        if MyButton.hover(center.x(MyButton.txt.w),center.y(MyButton.txt.h)):
            MyButton = button("Now Click!",32,color)
        if MyButton.click(center.x(MyButton.txt.w),center.y(MyButton.txt.h)):
            MyButton = button("YAY! You Got It!",32,color)
            clicks += 1
            color = list(color)
            if color[2] - 10 <= 0:
                color[1] -= 10
            if color[2] - 10 > 0:
                color[2] -= 10
            color = tuple(color)
        MyButton.render(center.x(MyButton.txt.w),center.y(MyButton.txt.h))
 #       msg = text(32,"Touch The Grass")
#        if (pygame.mouse.get_pos()[0] < (pygame.display.Info().current_w / 2) - (msg.w / 2) + msg.w and
 #           pygame.mouse.get_pos()[0] > (pygame.display.Info().current_w / 2) - (msg.w / 2) and
  #          pygame.mouse.get_pos()[1] < 2.5 * 100 + msg.h and
   #         pygame.mouse.get_pos()[1] > 2.5 * 100):
    #        msg.text_holder = "Now Click!"
     #      if pygame.mouse.get_pressed()[0]:
      #          msg.text_holder = "YAY!!"
       # msg.render((pygame.display.Info().current_w / 2) - (msg.w / 2), 2.5 * 100)

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