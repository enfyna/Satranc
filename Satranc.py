from time import sleep
import pygame
import Tahta
import sys

def tahta_ciz(display, tahta_boyutu, kare_boyutu):
    # Arkaplanı siyah yap
    display.fill((50, 50, 50))

    # Beyaz kareleri ciz
    for y in range(0, tahta_boyutu, kare_boyutu):
        baslangic = 0 if y // kare_boyutu % 2 == 0 else kare_boyutu
        for x in range(baslangic, tahta_boyutu, kare_boyutu * 2):
            pygame.draw.rect(display, (100, 100, 100), [x, y, kare_boyutu, kare_boyutu])

def taslari_ciz(display, taslar, kare_boyutu, font):
    konum = lambda a : a * kare_boyutu + (kare_boyutu // 2)
    for tas in taslar:
        yazi_yaz(display,tas.font_krt, tas.renk, None, 
            (konum(tas.posX),konum(tas.posY)),font)

def tehdit_edilen_kareleri_ciz(display, satranc_tahtasi, kare_boyutu):
    konum = lambda a : a * kare_boyutu + (2 * kare_boyutu // 5)
    boyut = kare_boyutu // 5
    for y in range(len(satranc_tahtasi)):
        for x in range(len(satranc_tahtasi)):
            if satranc_tahtasi[y][x][0] == None:
                continue
            elif satranc_tahtasi[y][x][0] == 0:
                renk = 75
            else:
                renk = satranc_tahtasi[y][x][0] * 125 + 125
            pygame.draw.rect(display, (renk,renk,renk),
                [konum(x), konum(y), boyut, boyut], border_radius=20)

def secili_tas_gidebileceği_yerleri_ciz(display,gidebilecegi_yerler,kare_boyutu):
    konum = lambda a : a * kare_boyutu + (3 * kare_boyutu // 7)
    boyut = kare_boyutu // 7
    for x, y in gidebilecegi_yerler:
        pygame.draw.rect(display, (255, 0, 0),
            [konum(x), konum(y), boyut, boyut], border_radius=20)

def yazi_yaz(display,yazi,renk,boyut,konum,font = None):
    if font == None:
        font = pygame.font.Font(pygame.font.get_default_font(), boyut)
    metin = font.render(yazi, True, renk)
    metin_dikdortgen = metin.get_rect()
    metin_dikdortgen.center = konum
    display.blit(metin, metin_dikdortgen)

def oyun_sonu_ekrani(display,takim,tahta_boyutu):
    renk = 50*-takim+100
    pygame.draw.rect(display,
        (renk,renk,renk),
        [10,10,tahta_boyutu-20,tahta_boyutu-20],
        border_radius=20
    )
    yazi = "Beyaz Kazandı." if takim == -1 else "Siyah Kazandı."
    yazi_yaz(display,yazi, (0,0,0), tahta_boyutu // 20, (tahta_boyutu/2,tahta_boyutu/2))
    
    yazi_yaz(display,"Oyunu kapatmak için tıkla.", (100,100,100), tahta_boyutu // 30, (tahta_boyutu/2,9*tahta_boyutu/10))
    pygame.display.flip()

def oyun_dongusu(display, tahta_boyutu, kare_boyutu, font):
    secili_tas, secili_tas_gidebilecegi_yerler = None, []
    sira = 0
    takimlar = [1, -1]

    satranc_tahtasi, taslar = Tahta.oyunu_baslat()

    ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, secili_tas_gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)

    kontrol = True
    while kontrol:
        events = pygame.event.get()
        if len(events) < 1:
            # Herhangi event yoksa bekle
            sleep(0.01)
            continue

        for event in events:
            if event.type == pygame.QUIT: 
                # Penceredeki kapatma tusuna basıldıysa oyunu kapat
                pygame.quit()
                return

        if not pygame.mouse.get_pressed()[0]:
            # Sol tık basılmamıssa devam etmeye gerek yok
            continue

        # Farenin tıkladığı konumu alalım
        x, y = map(lambda v: v // kare_boyutu, pygame.mouse.get_pos())
        
        if secili_tas and [x, y] in secili_tas_gidebilecegi_yerler:
            # Eğer seçili bir taşın gidebileceği bir konuma tıklandıysa
            # taşı oraya oynayalım ve oyun sırasını ilerletelim 
            Tahta.tasi_oyna(secili_tas, x, y, satranc_tahtasi)
            secili_tas, secili_tas_gidebilecegi_yerler = None, []
            sira += 1
            kontrol = ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, secili_tas_gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)
        else:
            # Eğer secili tas yoksa yada seçili taşın gidemeyeceği bir yere basılmışsa
            # Basılan yerde başka bir uygun taş varsa onu seç yoksa birşey yapma
            tasin_gidebileceği_yerler, tas_takimi = Tahta.gidebilecegi_yerler(x, y, satranc_tahtasi)

            if len(tasin_gidebileceği_yerler) > 0 and takimlar[sira % 2] == tas_takimi:
                secili_tas = (x, y)
                secili_tas_gidebilecegi_yerler = tasin_gidebileceği_yerler

        kontrol = ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, secili_tas_gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)
    
    while True:
        # Oyun bittikten sonra ekrana tiklanirsa oyunu kapat
        sleep(0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                return

def ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas=None, gidebilecegi_yerler=None, font=None, tahta_boyutu=400, kare_boyutu=50):
    k = Tahta.tahta_guncelle(satranc_tahtasi, taslar)
    if isinstance(k,int):
        oyun_sonu_ekrani(display,k,tahta_boyutu)
        return False

    tahta_ciz(display, tahta_boyutu, kare_boyutu)

    taslari_ciz(display, taslar, kare_boyutu, font)
    
    if globals()["tehdit_ciz"]:
        tehdit_edilen_kareleri_ciz(display, satranc_tahtasi, kare_boyutu)
    
    if secili_tas and gidebilecegi_yerler:
        secili_tas_gidebileceği_yerleri_ciz(display,gidebilecegi_yerler,kare_boyutu)

    pygame.display.flip()
    return True

tehdit_ciz : bool = False
def main():
    pygame.init()
    
    for i in sys.argv:
        if i.isdecimal():
            tahta_boyutu_arg = int(i)
        elif i == "-t":
            global tehdit_ciz
            tehdit_ciz = True
    
    tahta_boyutu : int = 600 if not locals().get("tahta_boyutu_arg") else tahta_boyutu_arg
    tahta_boyutu -= tahta_boyutu % 8 # 8e bölünebilir yap
    kare_boyutu : int = tahta_boyutu // 8
    display = pygame.display.set_mode([tahta_boyutu, tahta_boyutu])
    pygame.display.set_caption("Satranç")

    dosya_yolu : str = __file__.removesuffix("Satranc.py")
    font = pygame.font.Font(dosya_yolu+'merifont.ttf', tahta_boyutu // 10)
    
    oyun_dongusu(display, tahta_boyutu, kare_boyutu, font)

    return 0

if __name__ == '__main__':
    main()
