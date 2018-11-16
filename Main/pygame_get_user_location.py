import pygame

photopath = "Canteen-Recommender-App/Main/NTUcampus.png"

## define event handler for mouse click. 
## this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
   finish = False
   while finish == False:
   ## pygame.event.get() retrieves all events made by user
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        finish = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        finish = True

   return (mouseX, mouseY)


def get_user_location():
   
   ## make necessary initializations for Width, Height
   W = 990 # 990,1002
   H = 699 # 699, 707
   font = pygame.font.SysFont("monospace", 20)
   text1 = font.render("Canteen2", True, (0, 0, 0))
   
   # initialize display window, call it screen
   screen = pygame.display.set_mode((W, H))
   pygame.display.set_caption("Click on your current location")
   # read image file and rescale it to the window size
   screenIm = pygame.image.load(photopath)
   screenIm = pygame.transform.scale(screenIm, (W , H))
   
   # add the image over the screen object
   screen.blit(screenIm,(0, 0))   
   
   # add the text over the screen object
   screen.blit(text1 , (200,300))
   
   #will update the contents of the entire display window
   pygame.display.flip()
   
   # get outputs of Mouseclick event handler 
   buttonX, buttonY = MouseClick()
  #  print((buttonX , buttonY))
   
   return (buttonX , buttonY)

def main():
    pygame.init()
    print(get_user_location())

if __name__ == '__main__':
   main()