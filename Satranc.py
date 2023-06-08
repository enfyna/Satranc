from time import sleep
import pygame
import Tahta

def tahtayiciz(display):
    # Arkaplanı siyah yap
    display.fill((0,0,0))

    # Beyaz kareleri ciz
    for y in range(0,boardSize,squareSize): 
        start = 0 if y//squareSize % 2 == 0 else squareSize
        for x in range(start,boardSize,squareSize*2):
            pygame.draw.rect(display, (100 , 100 , 100), [x,y,squareSize,squareSize])

def taslariciz():
    for i in Tahta.tahtaGuncelle():
        renk = 25*i.takim+100

        pygame.draw.rect(display, 
            (renk , renk, renk), 
            [i.posX*squareSize+10,i.posY*squareSize+10,squareSize-20,squareSize-20],
            border_radius=20
        )        
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(i.isim, False, (0,0,0))
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = (i.posX*squareSize+squareSize/2,i.posY*squareSize+squareSize/2)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display.blit(text, textRect)

def ekranguncelle(display):
    tahtayiciz(display)
    taslariciz()
    # Flip the display
    pygame.display.flip()

pygame.init()

# Ekran ayarla
boardSize = 400
squareSize = boardSize // 8
display = pygame.display.set_mode([boardSize, boardSize])

# Font ayarla
font = pygame.font.Font('freesansbold.ttf', 32)

# Pencere başlığı 
pygame.display.set_caption("Satranç")

# Tahtayı baslat
Tahta.oyunuBaslat()

#Ekran çizdir
ekranguncelle(display)

running = True
while  running: # (taslar.bt(4) != 0 and taslar.st(4) != 0) and
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Did the user click the window close button?
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                x , y = pygame.mouse.get_pos()
                print("Left Mouse key was clicked at " + str(x) + " ," + str(y)) 
                ekranguncelle(display)
    sleep(.1)

pygame.quit()