import pygame
import sys
import time
import random

pygame.init()

white = (255, 255, 255)
black = (100, 0, 0)
red = (255, 0, 0)
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("snake")
font = pygame.font.SysFont(None, 25, bold=True)


def myquit():
    pygame.quit()
    sys.exit(0)


clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0


def snake(blockSize, snakeList):
    for size in snakeList:
        pygame.draw.rect(gameDisplay, black, [size[0]+5, size[1, blockSize]])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakeList = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_height-blockSize))
    randomAppleY = round(random.randrange(0, window_height-blockSize))

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over,press C to play again or Q to Quit")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif downArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill(white)

        AppleThcikness = 20

        print([int(randomAppleX), int(randomAppleY), AppleThcikness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX, randomAppleY])

        allspritesList = []
        allspritesList.append(lead_x)
        allspritesList.append(lead_y)
        snakeList.append(allspritesList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == allspritesList:
                gameOver = True

        snake(blockSize, snakeList)

        pygame.display.update()

        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThcikness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThcikness:
                randomAppleX = round(random.randrange(0, window_width))
                randomAppleY = round(random.randrange(0, window_height))
                snakeLength += 1

        clock.tick(FPS)
    pygame.quit()
    quit()


gameLoop()
