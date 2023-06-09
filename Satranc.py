from time import sleep
import pygame
import Tahta

## 1- Tas Sec fonksiyonu ekle ona gore gidilebilen yerleri ciz

## 2- Ondan sonra cizilen kareleri kaydet eger oyucu cizilen kareye tiklarsa tasi oraya oyna

## 3- Sıra ekle beyaz siyah arasında

## 4- Şah çekme ve oyunun bitmesini ekle

def tahtayiciz(display):
    # Arkaplanı siyah yap
    display.fill((0,0,0))

    # Beyaz kareleri ciz
    for y in range(0,boardSize,squareSize):
        start = 0 if y//squareSize % 2 == 0 else squareSize
        for x in range(start,boardSize,squareSize*2):
            pygame.draw.rect(display, (100 , 100 , 100), [x,y,squareSize,squareSize])

def taslariciz():
    for i in Tahta.tahtaGuncelle(tahta , taslar):
        renk = 50*i.takim+100

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

def gidilebilenyerlericiz(x,y):
    for i in Tahta.gidebilir(x,y,tahta):
        renk = (255,0,0)
        pygame.draw.rect(display,renk,
            [i[0]*squareSize+30,i[1]*squareSize+30,squareSize-60,squareSize-60],
            border_radius=20
        )
    pass
def tehditedilenyerlericiz():
    for j in taslar:
        for i in j.gidebilir():
            renk = max(50,255*j.takim)
            pygame.draw.rect(display,(renk,renk,renk),
                [i[0]*squareSize+30,i[1]*squareSize+30,squareSize-60,squareSize-60],
                border_radius=20
            )
    pass

def ekranguncelle(display,x = None ,y = None):
    tahtayiciz(display)
    taslariciz()

    tehditedilenyerlericiz()
    if x != None and y != None:
        gidilebilenyerlericiz(x,y)

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
tahta , taslar = Tahta.oyunuBaslat()

#Ekran çizdir
ekranguncelle(display)

running = True
while running: # (taslar.bt(4) != 0 and taslar.st(4) != 0) and
    sleep(.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Pencerenin X butonuna basıldıysa devam etmeye gerek yok
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                x , y = map(lambda v : v // squareSize , pygame.mouse.get_pos())
                ekranguncelle(display,x,y)

pygame.quit()
