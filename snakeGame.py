import pygame
import random
import math

pygame.init()

displayHeight = 800
displayWidth = 1000

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.update()
pygame.display.set_caption('Snake Game')


snakeGreen = (50, 205, 50)
black = (0, 0, 0)
red = (255, 0, 0)
lightViolet = (207, 159, 255)


calibri_font_large = pygame.font.SysFont('Calibri', 60, False, False)
calibri_font_small = pygame.font.SysFont('Calibri', 30, False, False)

snakeSpeed = 15
snakeRadius = 15
clock = pygame.time.Clock()

def displayScore(score):
    loseText = calibri_font_small.render("Score: " + str(score), True, lightViolet)
    display.blit(loseText, [30, 30])

def drawSnake(snakeList):
    for pos in snakeList:
        pygame.draw.circle(display, snakeGreen, (pos[0], pos[1]), snakeRadius)

def game():
    xPos = displayWidth / 2
    yPos = displayHeight / 2
    dy = 0
    dx = 0
    gameOver = False
    closeGame = False
    foodXlocation = random.randrange(1, displayWidth - 1)
    foodYlocation = random.randrange(1, displayHeight - 1)
    snakeList = []
    snakeLength = 1
    score = 0
    

    while not gameOver:

        while closeGame == True:

            display.fill(black)
            loseText = calibri_font_large.render("You lose!", True, red)
            display.blit(loseText, [displayWidth / 2 - 140, displayHeight / 2 - 100])
            restText = calibri_font_small.render("Click C to continue or Q to quit playing", True, red)
            display.blit(restText, [displayWidth / 2 - 240, displayHeight / 2])
            scoreText = calibri_font_small.render("Your final score was: " + str(score), True, red)
            display.blit(scoreText, [displayWidth / 2 - 170, displayHeight / 2 + 55])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        closeGame = False
                        gameOver = True
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    dx = 0
                    dy = snakeSpeed
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -snakeSpeed
                elif event.key == pygame.K_LEFT:
                    dx = -snakeSpeed
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snakeSpeed
                    dy = 0
        xPos += dx
        yPos += dy
        display.fill(black)
        if yPos < 0 or yPos > displayHeight or xPos < 0 or xPos > displayWidth:
            closeGame = True

        pygame.draw.circle(display, red, (foodXlocation, foodYlocation), snakeRadius) # draw food

        snakeHead = []
        snakeHead.append(xPos)
        snakeHead.append(yPos)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Checks if head is overlapping the body where pos is == to snakeHead position
        for pos in snakeList[:-1]:
            if pos == snakeHead:        
                closeGame = True
        
        distance = math.sqrt(pow(xPos - foodXlocation, 2) + pow(yPos - foodYlocation, 2))

        if distance < 2 * snakeRadius:
            # draw food again and increase snake length
            foodXlocation = random.randrange(1, displayWidth - 1)
            foodYlocation = random.randrange(1, displayHeight - 1)
            snakeLength += 1
            score += 1

        drawSnake(snakeList)
        displayScore(score)
        pygame.display.update()

        clock.tick(snakeSpeed)

    # quits application
    pygame.quit()
    quit()

game()