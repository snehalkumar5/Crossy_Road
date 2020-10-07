import math
import time

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("CROSSY ROADIES")
icon = pygame.image.load('p1.png')
pygame.display.set_icon(icon)

# background music
mixer.music.load("bgsong.mp3")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('p1.png')
playerX = 370
playerY = 560
playerX_change = 0
playerY_change = 0
player2Img = pygame.image.load('p2.png')
player2X = 370
player2Y = 15
player2X_change = 0
player2Y_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 11

for i in range(num_of_enemies):
    # if i == 0:
    enemyImg.append(pygame.image.load('car.png'))
    enemyX.append(50)
    enemyY.append(490)
    enemyX_change.append(6)

    # if i == 1:
    enemyImg.append(pygame.image.load('car1.png'))
    enemyX.append(780)
    enemyY.append(380)
    enemyX_change.append(-8)

    # if i == 2:
    enemyImg.append(pygame.image.load('car1.png'))
    enemyX.append(500)
    enemyY.append(160)
    enemyX_change.append(-8)

    # if i == 3:
    enemyImg.append(pygame.image.load('car.png'))
    enemyX.append(600)
    enemyY.append(270)
    enemyX_change.append(8)

    # if i == 4:
    enemyImg.append(pygame.image.load('car2.png'))
    enemyX.append(200)
    enemyY.append(50)
    enemyX_change.append(9)

    enemyImg.append(pygame.image.load('tree.png'))
    enemyX.append(480)
    enemyY.append(110)
    enemyImg.append(pygame.image.load('tree.png'))
    enemyX.append(70)
    enemyY.append(440)
    enemyImg.append(pygame.image.load('tree.png'))
    enemyX.append(370)
    enemyY.append(220)
    enemyImg.append(pygame.image.load('snake.png'))
    enemyX.append(150)
    enemyY.append(212)
    enemyImg.append(pygame.image.load('snake.png'))
    enemyX.append(440)
    enemyY.append(430)
    enemyImg.append(pygame.image.load('tree.png'))
    enemyX.append(600)
    enemyY.append(340)

# safe blocks
block = pygame.Rect(0, 0, 800, 54.5)
block1 = pygame.Rect(0, 109, 800, 54.5)
block2 = pygame.Rect(0, 218, 800, 54.5)
block3 = pygame.Rect(0, 327, 800, 54.5)
block4 = pygame.Rect(0, 436, 800, 54.5)
block5 = pygame.Rect(0, 545.5, 800, 54.5)
bcolor = (0, 200, 0)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)

text1X = 10
text1Y = 10
text2X = 560
text2Y = 560

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
