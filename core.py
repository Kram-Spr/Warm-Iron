import pygame
import os 

pygame.display.init()
clock = pygame.time.Clock()
user_screen = pygame.display.Info()
win = pygame.display.set_mode((user_screen.current_w - 50,user_screen.current_h - 100))
pygame.display.set_caption('Warm Iron')

def refresher(plr_x,plr_y):
    global user_screen
    win.fill((183, 82, 30))
    player_sprite = pygame.image.load('sprites\player.png')
    player_sprite = pygame.transform.scale(player_sprite, (user_screen.current_w // 5, user_screen.current_h // 4))
    win.blit(player_sprite, (50 + plr_x,(user_screen.current_h - 400) + plr_y))
    pygame.display.update()

def main():
    running = True
    clock.tick(60)

    moving_left = False
    moving_right = False
    plr_x = 0
    plr_y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 100:
                    moving_right = False
                    moving_left = True
                elif event.key == 97:
                    moving_left = False
                    moving_right = True
            elif event.type == pygame.KEYUP:
                moving_left = False
                moving_right = False

            if moving_left:
                plr_x += 5
            elif moving_right:
                plr_x -= 5

        refresher(plr_x, plr_y)

main()