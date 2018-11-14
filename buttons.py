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

    buttonText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, buttonText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)