from config import *


# show score for player 1
def show_score1():
    score = font.render("Player 1 Score : " + str(player1s), True, (255, 255, 255))
    screen.blit(score, (10, 10))


# show score for player 2
def show_score2():
    score = font.render("Player 2 Score : " + str(player2s), True, (255, 255, 255))
    screen.blit(score, (560, 560))


# GAMEOVER DISPLAY
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# DISPLAY WINNER
def winner():
    player1s = int(scorep1r1 + scorep1r2)
    player2s = int(scorep2r1 + scorep2r2)
    over = font.render("FINAL SCORES:", True, (0, 255, 255))
    P1 = font.render("Player 1: " + str(player1s), True, (0, 255, 255))
    P2 = font.render("Player 2: " + str(player2s), True, (0, 255, 255))
    screen.blit(over, (150, 100))
    screen.blit(P1, (150, 125))
    screen.blit(P2, (150, 150))

    if player1s > player2s:
        over_text = over_font.render("Player 1 WINS", True, (255, 255, 255))
    elif player1s == player2s:
        over_text = over_font.render("GAME TIED", True, (255, 255, 255))
    else:
        over_text = over_font.render("Player 2 WINS", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Game intro screen
def intro():
    over_text1 = font.render("CROSSY ROADIES", True, (255, 255, 255))
    over_text2 = font.render("Game by Snehal Kumar", True, (255, 255, 255))
    over_text3 = font.render("Press SPACE to play..", True, (255, 255, 255))
    over_text4 = font.render("Use arrow keys to move", True, (255, 255, 255))
    screen.blit(over_text1, (275, 125))
    screen.blit(over_text2, (250, 250))
    screen.blit(over_text3, (268, 350))
    screen.blit(over_text4, (250, 400))


# player1
def player(x, y):
    screen.blit(playerImg, (x, y))


# player 2
def player2(x, y):
    screen.blit(player2Img, (x, y))


# enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# function to detect collision
def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False


def isCollision1(enemyX, enemyY, player2X, player2Y):
    distance = math.sqrt(math.pow(enemyX - player2X, 2) + (math.pow(enemyY - player2Y, 2)))
    if distance < 30:
        return True
    else:
        return False


# Variables initialisation
player1s = 0
player2s = 0
p1r1 = 0
p1r2 = 0
p2r1 = 0
p2r2 = 0
count = 0
col1 = 0
col2 = 0
flag = 0
rounds = 0
number = 0
scorep1r1 = 0
scorep1r2 = 0
scorep2r1 = 0
scorep2r2 = 0
g = 0
tt = 0
p2v = 0
p1v = 0
introd = True
running = True
timer = 0

# -----------------------------------------------------
#                       GAME INTRO
# -----------------------------------------------------
while introd:
    timer = pygame.time.get_ticks()
    pygame.time.delay(20)
    screen.fill((0, 0, 0))
    intro()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            introd = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                introd = False
    pygame.display.update()

# ------------------------------------------------------------------------
#                              GAME LOOP
# ------------------------------------------------------------------------
while running:
    pygame.time.delay(20)
    if introd == False:
        seconds = (pygame.time.get_ticks() - timer) / 1000
    # RGB = Red, Green, Blue
    screen.fill((51, 44, 44))

    if flag > count:
        count = flag
        seconds = 0
    if g == 8:
        playerX = 370
        playerY = 560
        g = 0

    if g == 5:
        player2X = 370
        player2Y = 15
        g = 0
    if g == 2:
        playerX = 370
        playerY = 560
        g = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ------------------------------------------------------------------------
        #                       PLAYER MOVEMENT
        # ------------------------------------------------------------------------

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if flag % 2 == 0:
                    playerX -= 60
                else:
                    player2X -= 60
            elif event.key == pygame.K_RIGHT:
                if flag % 2 == 0:
                    playerX += 60
                else:
                    player2X += 60
            elif event.key == pygame.K_UP:
                if flag % 2 == 0:
                    playerY -= 54.5
                else:
                    player2Y -= 54.5
            elif event.key == pygame.K_DOWN:
                if flag % 2 == 0:
                    playerY += 54.5
                else:
                    player2Y += 54.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                player2X_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
                player2Y_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 0:
        playerY = 15
    elif playerY >= 560:
        playerY = 560

    player2X += player2X_change
    if player2X <= 0:
        player2X = 0
    elif player2X >= 736:
        player2X = 736
    player2Y += player2Y_change
    if player2Y <= 0:
        player2Y = 15
    elif player2Y >= 560:
        player2Y = 560

    # ----------------------------------------------------------
    #                   ENEMY MOVEMENT
    # ----------------------------------------------------------
    for i in range(num_of_enemies):

        if i == 0:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] >= 810:
                enemyX[i] = -30
            if p1r1 > 0 and flag % 2 == 0:
                enemyX_change[i] = 10
            elif p2r1 > 0 and flag % 2 == 1:
                enemyX_change[i] = 10
            else:
                enemyX_change[i] = 6

        elif i == 1:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= -30:
                enemyX[i] = 1000
            if p1r1 > 0 and flag % 2 == 0:
                enemyX_change[i] = -12
            elif p2r1 > 0 and flag % 2 == 1:
                enemyX_change[i] = -12
            else:
                enemyX_change[i] = -8
        elif i == 2:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= -50:
                enemyX[i] = 1000
            if p1r1 > 0 and flag % 2 == 0:
                enemyX_change[i] = -14
            elif p2r1 > 0 and flag % 2 == 1:
                enemyX_change[i] = -14
            else:
                enemyX_change[i] = -8
        elif i == 3:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] >= 810:
                enemyX[i] = -15
            if p1r1 > 0 and flag % 2 == 0:
                enemyX_change[i] = 14
            elif p2r1 > 0 and flag % 2 == 1:
                enemyX_change[i] = 14
            else:
                enemyX_change[i] = 8
        elif i == 4:
            enemyX[i] += enemyX_change[i]
            if enemyX[i] >= 810:
                enemyX[i] = -15
            if p1r1 > 0 and flag % 2 == 0:
                enemyX_change[i] = 16
            elif p2r1 > 0 and flag % 2 == 1:
                enemyX_change[i] = 16
            else:
                enemyX_change[i] = 9

        # ---------------------------------------------------------------------------------------------------
        #                    COLLISION
        # ---------------------------------------------------------------------------------------------------
        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision:
            explosionSound = mixer.Sound("headchop.wav")
            explosionSound.play()
            playerY = 560
            playerX = 370
            flag += 1

        collision1 = isCollision1(enemyX[i], enemyY[i], player2X, player2Y)
        if collision1:
            explosionSound = mixer.Sound("headchop.wav")
            explosionSound.play()
            player2Y = 15
            player2X = 370
            flag += 1
    # ---------------------------------------------------------------------------------------------------
    #                  POINTS SYSTEM
    # ---------------------------------------------------------------------------------------------------
    # FOR PLAYER 1
    if flag % 2 == 0:
        if playerY <= 15:
            p1pnts = 250
            if p1v == 0:
                p1r1 = 1
                p1v += 1
            elif p1v > 0 and number == 2:
                p1r2 = 1
        elif playerY <= 124:
            p1pnts = 100
        elif playerY <= 233:
            p1pnts = 75
        elif playerY <= 342:
            p1pnts = 50
        elif playerY <= 451:
            p1pnts = 25
        else:
            p1pnts = 0
    # FOR PLAYER 2
    if flag % 2 == 1:
        if player2Y >= 560:
            p2pnts = 250
            if p2v == 0:
                p2r1 = 1
                p2v += 1
            elif p2v > 0 and number == 3:
                p2r2 = 1
        elif player2Y >= 451:
            p2pnts = 100
        elif player2Y >= 342:
            p2pnts = 75
        elif player2Y >= 233:
            p2pnts = 50
        elif player2Y >= 124:
            p2pnts = 25
        else:
            p2pnts = 0
    # ----------------------------------------------------
    #               SCORING SYSTEM
    # ----------------------------------------------------
    if number == 0:
        scorep1r1 = p1pnts - seconds
        t1 = seconds
    if number == 1:
        scorep2r1 = p2pnts - seconds + t1
        t2 = seconds
    if number == 2:
        scorep1r2 = p1pnts - seconds + t2
        t3 = seconds
    if number == 3:
        scorep2r2 = p2pnts - seconds + t3

    # safe roads
    pygame.draw.rect(screen, bcolor, block)
    pygame.draw.rect(screen, bcolor, block1)
    pygame.draw.rect(screen, bcolor, block2)
    pygame.draw.rect(screen, bcolor, block3)
    pygame.draw.rect(screen, bcolor, block4)
    pygame.draw.rect(screen, bcolor, block5)

    # set flags if player reaches end successfully
    for i in range(num_of_enemies):
        enemy(enemyX[i], enemyY[i], i)

    if p1r1 == 1:
        flag += 1
        p1r1 = 2
    if p1r2 == 1:
        flag += 1
        p1r2 = 2
    if p2r1 == 1:
        flag += 1
        p2r1 = 2
    if p2r2 == 1:
        flag += 1
        p2r2 = 2
    # Show player character after each round
    if flag % 2 == 0:
        player(playerX, playerY)
    elif flag % 2 == 1:
        player2(player2X, player2Y)

    # Display scores of players
    show_score1()
    show_score2()
    # print(player1s)
    # print(player2s)
    if flag == 2:
        g = flag
        flag += 2
    if flag == 5:
        g = flag
        flag += 2
    if flag == 8:
        g = flag
    if flag > rounds:
        rounds = flag
        number += 1
    player1s = int(scorep1r1 + scorep1r2)
    player2s = int(scorep2r1 + scorep2r2)

    # GameOver
    if number == 4:
       screen.fill((0,0,0))
       winner()
    pygame.display.update()
