import pygame
import math
import os
pygame.display.init()
clock = pygame.time.Clock()

class Screen():
    def __init__(self,sWidth,sHeight,mouse_x,mouse_y):
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.win = pygame.display.set_mode((self.sWidth,self.sHeight))
        pygame.display.set_caption('Warm Iron')
        self.refresher(mouse_x,mouse_y)

    def refresher(self,mouse_x,mouse_y):
        self.win.fill((183, 82, 30))
        plr_arm = Arm(mouse_x,mouse_y)
        self.player_sprite = pygame.image.load('sprites\player.png')
        self.player_sprite = pygame.transform.scale(self.player_sprite, (320,320))
        self.win.blit(self.player_sprite, (50,300))
        self.win.blit(plr_arm.roArm_line,plr_arm.orig_pos)
        pygame.display.update()

class Arm():
    def __init__(self,mouse_x,mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.arm_line = pygame.image.load('assets\line.png')
        self.arm_line = pygame.transform.scale(self.arm_line, (230,20))
        self.rotate()

    def rotate(self):
        #rel_x, rel_y = self.mouse_x - 1500, self.mouse_y - 750
        #angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        rel_x, rel_y = pygame.mouse.get_pos() - pygame.math.Vector2(130,500)
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        self.roArm_line = pygame.transform.rotate(self.arm_line, int(angle))
        self.orig_pos = self.arm_line.get_rect(center = self.arm_line.get_rect().center)
        self.orig_pos = self.orig_pos.move(130,500)
        #Rectangle blitted to is not moving alongside line? creating cap?

def main():
    running = True
    clock.tick(60)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse = pygame.mouse.get_pos()
        screen = Screen(1500,750,mouse[0],mouse[1])

main()