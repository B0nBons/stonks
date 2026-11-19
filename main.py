import random
import os
import time
import pygame # were using pygame ce
from bank import Bank
from stonks import StockMarket

pygame.init()
# this is genuinely like old trauma

screen = pygame.display.set_mode((800, 800)) # pygame loves tuples
clock = pygame.time.Clock()

# player start
x = 400
y = 400
speed = 2

# ok first thing i wanna do is just make some background assets for the cool layer bg effect

while True:
    for event in pygame.event.get():
        pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_d]:
        x += speed
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,0),(x,y,40,40))

    pygame.display.flip()
    clock.tick(30)
