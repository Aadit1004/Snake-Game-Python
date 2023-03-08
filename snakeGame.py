import pygame

pygame.init()

displayHeight = 800
displayWidth = 1000

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.update()
pygame.display.set_caption('Snake Game')


snakeGreen = (50, 205, 50)
black = (0, 0, 0)

xPos = displayWidth / 2
yPos = displayHeight / 2

dy = 0
dx = 0

snakeSpeed = 10
snakeRadius = 15
clock = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        display.fill(black)
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
    pygame.draw.circle(display, snakeGreen, (xPos, yPos), snakeRadius)
    pygame.display.update()
    clock.tick(snakeSpeed)

# quits application
pygame.quit()
quit()