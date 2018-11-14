import pygame
from pygame.locals import *
import time

pygame.init()

display_width = 450
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

burger_width = 20
burger_height = 20

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Test')

clock = pygame.time.Clock()
ImgRaw = pygame.image.load('burger.png')
Img = pygame.transform.scale(ImgRaw, (burger_width, burger_height))


def displaymap():
    mapp = pygame.image.load("NTUcampus2.jpg")
    mapp = pygame.transform.scale(mapp, (display_width, display_height))

    gameDisplay.blit(mapp,(0,0))

def quitapp():
    pygame.quit()
    quit()

def burger(x,y):
    gameDisplay.blit(Img, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/5))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def button(msg, x, y, w, h, inactive_colour, active_colour, action=None):
    mouse = pygame.mouse.get_pos() # (x coordinate, y coordinate)
    click = pygame.mouse.get_pressed() # (left button, middle scroll button, right button)
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_colour, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            if action == "play":
                game_loop()

    else:
        pygame.draw.rect(gameDisplay, inactive_colour, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Start Menu", largeText)
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 50,350,150,75, green, bright_green, game_loop)
        button("Quit", 250,350,150,75, red, bright_red, quitapp)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.55

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        
        x += x_change 
        y += y_change

        displaymap()
        burger(x, y)

        if x > display_width - burger_width:
            x = display_width - burger_width
        elif x < 0:
            x = 0

        if y > display_height - burger_height:
            y = display_height - burger_height
        elif y < 0:
            y = 0

        pygame.display.flip()
        clock.tick(240)

game_intro()
game_loop()
pygame.quit()