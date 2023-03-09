import pygame
import random

pygame.init()

displayHeight = 800
displayWidth = 1000

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.update()
pygame.display.set_caption('Snake Game')


snakeGreen = (50, 205, 50)
black = (0, 0, 0)
red = (255, 0, 0)


calibri_font_large = pygame.font.SysFont('Calibri', 60, False, False)
calibri_font_small = pygame.font.SysFont('Calibri', 30, False, False)

snakeSpeed = 15
snakeRadius = 15
clock = pygame.time.Clock()

def game():
    xPos = displayWidth / 2
    yPos = displayHeight / 2
    dy = 0
    dx = 0
    gameOver = False
    closeGame = False
    foodXlocation = random.randrange(1, displayWidth - 1)
    foodYlocation = random.randrange(1, displayHeight - 1)

    while not gameOver:

        while closeGame == True:

            display.fill(black)
            loseText = calibri_font_large.render("You lose!", True, red)
            display.blit(loseText, [displayWidth / 2 - 140, displayHeight / 2 - 100])
            restText = calibri_font_small.render("Click C to continue or Q to quit playing", True, red)
            display.blit(restText, [displayWidth / 2 - 240, displayHeight / 2])

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
        pygame.draw.circle(display, snakeGreen, (xPos, yPos), snakeRadius)
        pygame.draw.circle(display, red, (foodXlocation, foodYlocation), snakeRadius)
        pygame.display.update()

        if xPos == foodXlocation and yPos == foodYlocation:
            print("Captured food!")
        clock.tick(snakeSpeed)

    # quits application
    pygame.quit()
    quit()

game()