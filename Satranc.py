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
    t = Tahta.tahtaGuncelle(tahta , taslar)
    if isinstance(t,int):
        pygame.draw.rect(display,
            (50*t+100 ,50*t+100  , 50*t+100 ),
            [10,10,boardSize-20,boardSize-20],
            border_radius=20
        )
        t = "Beyaz" if t == 1 else "Siyah"
        text = font.render(str(t)+str(" Kaybetti."), False, (0,0,0))

        textRect = text.get_rect()

        textRect.center = (boardSize/2,boardSize/2)

        display.blit(text, textRect)
        return
    for i in t:
        renk = 50*i.takim+100

        pygame.draw.rect(display,
            (renk , renk, renk),
            [i.posX*squareSize+10,i.posY*squareSize+10,squareSize-20,squareSize-20],
            border_radius=20
        )
        text = font.render(i.isim, False, (0,0,0))

        textRect = text.get_rect()

        textRect.center = (i.posX*squareSize+squareSize/2,i.posY*squareSize+squareSize/2)

        display.blit(text, textRect)

def tehditedilenyerlericiz():
    for j in taslar:
        for i in j.gidebilir():
            renk = max(50,255*j.takim)
            pygame.draw.rect(display,(renk,renk,renk),
                [i[0]*squareSize+30,i[1]*squareSize+30,squareSize-60,squareSize-60],
                border_radius=20
            )

def oyun(x,y):
    global seciliTas
    global gidebilir
    global sira
    global takim
    # Secili tas varsa ve bu tasin gidebileceği bir 
    # konuma tiklanmissa tasi oraya gotur
    if seciliTas:  
        if len(gidebilir) < 0:
            return
        if [x,y] in gidebilir:
            Tahta.gotur(seciliTas,x,y,tahta)
            sira += 1
            seciliTas = ()
            gidebilir = []
            ekranguncelle(display)
            return
    # Secili tas yoksa 
    # Tiklanan karede tas varsa onu sec ve gidebilecegi yerleri hesapla ve goster
    gidebilir , tastakim = Tahta.gidebilir(x, y, tahta)
    if len(gidebilir) == 0:
        return
    if takim[sira%2] == tastakim: 
        seciliTas = (x,y)
        for i in gidebilir:
            renk = (255,0,0)
            pygame.draw.rect(display,renk,
                [i[0]*squareSize+30,i[1]*squareSize+30,squareSize-60,squareSize-60],
                border_radius=20
            )
    pass

def ekranguncelle(display,x = None ,y = None):
    tahtayiciz(display)
    taslariciz()
    #tehditedilenyerlericiz()
    if x != None and y != None:
        oyun(x,y)

    Tahta.yazdir(tahta, taslar)

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

# Oyun değişkenleri
seciliTas : tuple = ()
gidebilir : list = []
takim : list = [1,-1]
sira : int = 0

# Tahtayı baslat
tahta , taslar = Tahta.oyunuBaslat()

#Ekran çizdir
ekranguncelle(display)

running = True
while running:
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
