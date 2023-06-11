from time import sleep
import pygame
import Tahta

def tahta_ciz(display, tahta_boyutu, kare_boyutu):
    # Arkaplanı siyah yap
    display.fill((0, 0, 0))

    # Beyaz kareleri ciz
    for y in range(0, tahta_boyutu, kare_boyutu):
        baslangic = 0 if y // kare_boyutu % 2 == 0 else kare_boyutu
        for x in range(baslangic, tahta_boyutu, kare_boyutu * 2):
            pygame.draw.rect(display, (100, 100, 100), [x, y, kare_boyutu, kare_boyutu])

def taslari_ciz(display, taslar, kare_boyutu, font):
    for tas in taslar:
        renk = 50 * tas.takim + 100

        pygame.draw.rect(display, (renk, renk, renk),
                         [tas.posX * kare_boyutu + 10, tas.posY * kare_boyutu + 10,
                          kare_boyutu - 20, kare_boyutu - 20], border_radius=20)

        metin = font.render(tas.isim, False, (0, 0, 0))
        metin_dikdortgen = metin.get_rect()
        metin_dikdortgen.center = (tas.posX * kare_boyutu + kare_boyutu / 2,
                                   tas.posY * kare_boyutu + kare_boyutu / 2)
        display.blit(metin, metin_dikdortgen)

def tehdit_edilen_kareleri_ciz(display, taslar, kare_boyutu):
    for tas in taslar:
        for pozisyon in tas.gidebilecegi_yerler():
            renk = max(50, 255 * tas.takim)
            pygame.draw.rect(display, (renk, renk, renk),
                             [pozisyon[0] * kare_boyutu + 30, pozisyon[1] * kare_boyutu + 30,
                              kare_boyutu - 60, kare_boyutu - 60], border_radius=20)

def secili_tas_gidebileceği_yerleri_ciz(display,gidebilecegi_yerler,kare_boyutu):
    for gidilecek_yer in gidebilecegi_yerler:
        pygame.draw.rect(display, (255, 0, 0),
            [gidilecek_yer[0] * kare_boyutu + 30, gidilecek_yer[1] * kare_boyutu + 30,
            kare_boyutu - 60, kare_boyutu - 60], border_radius=20)

def oyun_sonu_ekrani(display,takim,tahta_boyutu,font):
    renk = 50*-takim+100
    pygame.draw.rect(display,
        (renk,renk,renk),
        [10,10,tahta_boyutu-20,tahta_boyutu-20],
        border_radius=20
    )
    takim = "Beyaz Kazandı." if takim == -1 else "Siyah Kazandı."
    text = font.render(str(takim), False, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (tahta_boyutu/2,tahta_boyutu/2)
    display.blit(text, textRect)

    text = font.render("Oyunu kapatmak için tıkla.", False, (75,75,75))
    textRect = text.get_rect()
    textRect.center = (tahta_boyutu/2,9*tahta_boyutu/10)
    display.blit(text, textRect)
    pygame.display.flip()

def oyun_dongusu(display, tahta_boyutu, kare_boyutu, font):
    secili_tas = None
    gidebilecegi_yerler = []
    sira = 0
    takimlar = [1, -1]

    satranc_tahtasi, taslar = Tahta.oyunu_baslat()

    ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)

    kontrol = True
    while kontrol:
        sleep(0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_tiklamalari = pygame.mouse.get_pressed()

                if mouse_tiklamalari[0]:
                    x, y = map(lambda v: v // kare_boyutu, pygame.mouse.get_pos())
                    if secili_tas:
                        if [x, y] in gidebilecegi_yerler:
                            Tahta.tasi_oyna(secili_tas, x, y, satranc_tahtasi)
                            sira += 1
                            secili_tas = None
                            gidebilecegi_yerler = []
                            kontrol = ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)
                            continue
                        secili_tas = None

                    gidebilecegi_yerler, tas_takimi = Tahta.gidebilecegi_yerler(x, y, satranc_tahtasi)

                    if not gidebilecegi_yerler:
                        continue

                    if takimlar[sira % 2] == tas_takimi:
                        secili_tas = (x, y)

                kontrol = ekran_guncelle(display, satranc_tahtasi, taslar, secili_tas, gidebilecegi_yerler, font, tahta_boyutu, kare_boyutu)
    
    while True:
        # Oyun bittikten sonra ekrana  
        # tiklanirsa oyunu kapat
        sleep(0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                return
    

def ekran_guncelle(display, satranc_tahtasi=None, taslar=None, secili_tas=None, gidebilecegi_yerler=None, font=None, tahta_boyutu=400, kare_boyutu=50):
    k = Tahta.tahta_guncelle(satranc_tahtasi, taslar)
    if isinstance(k,int):
        oyun_sonu_ekrani(display,k,tahta_boyutu,font)
        return False
    tahta_ciz(display, tahta_boyutu, kare_boyutu)
    if satranc_tahtasi and taslar:
        taslari_ciz(display, taslar, kare_boyutu, font)
        #tehdit_edilen_kareleri_ciz(display, taslar, kare_boyutu)
        if secili_tas and gidebilecegi_yerler:
            secili_tas_gidebileceği_yerleri_ciz(display,gidebilecegi_yerler,kare_boyutu)
    
    if satranc_tahtasi:
        #Tahta.tehdit_yazdir(satranc_tahtasi, taslar)
        pass

    pygame.display.flip()
    return True

def main():
    pygame.init()

    tahta_boyutu = 600
    kare_boyutu = tahta_boyutu // 8
    display = pygame.display.set_mode([tahta_boyutu, tahta_boyutu])
    font = pygame.font.Font('freesansbold.ttf', 32)
    pygame.display.set_caption("Satranç")

    oyun_dongusu(display, tahta_boyutu, kare_boyutu, font)
    
    pygame.quit()

    return 0

if __name__ == '__main__':
    main()
