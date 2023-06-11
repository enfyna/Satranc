import Tas

def oyunu_baslat():
    tahta = [[[None,0] for _ in range(8)] for _ in range(8)]
    # tahta[y][x][tehdit][tas]
    # y : tahta y ekseni
    # x : tahta x ekseni
    # tehdit : tahtadaki taslarin tehditlerine gore 
    # None, 1, -1 ve ya 0 olabilir
    # tas : o karede bulunan tasi gosterir
    taslar = []

    for i in range(8):
        taslar.append(Tas.Piyon(i, 1, 1, tahta))
        taslar.append(Tas.Piyon(i, 6, -1, tahta))
    for i in range(2):
        taslar.append(Tas.Kale(i*7, 0, 1, tahta))
        taslar.append(Tas.Kale(i*7, 7, -1, tahta))
    for i in range(1,7,5):
        taslar.append(Tas.At(i, 0, 1, tahta))
        taslar.append(Tas.At(i, 7, -1, tahta))
    for i in range(2,6,3):
        taslar.append(Tas.Fil(i, 0, 1, tahta))
        taslar.append(Tas.Fil(i, 7, -1, tahta))

    taslar.append(Tas.Şah(4, 7, -1, tahta))
    taslar.append(Tas.Vezir(3, 7, -1, tahta))

    taslar.append(Tas.Şah(4, 0, 1, tahta))
    taslar.append(Tas.Vezir(3, 0, 1, tahta))

    tahta_guncelle(tahta, taslar)

    return tahta , taslar

def tahta_guncelle(tahta , taslar):
    for i in range(len(tahta)): # tahtayi sifirla
        for j in range(len(tahta[i])):
            tahta[i][j][0] = None
            tahta[i][j][1] = 0

    for i in taslar: # Taslari diz
        if i.yasiyor: # Tas yasiyorsa tahtaya koy
            tahta[i.posY][i.posX][1] = i
            continue
        if isinstance(i, Tas.Şah):
            return i.takim
        taslar.remove(i) # Yasamiyorsa listeden cikar

    for i in taslar: # Taslarin tehditlerini hesapla
        i.tehdit()

    return taslar

def gidebilecegi_yerler(x,y,tahta):
    if isinstance(tahta[y][x][1],Tas.Tas):
        return tahta[y][x][1].gidebilecegi_yerler() , tahta[y][x][1].takim
    return [] , None

def tasi_oyna(tk,x,y,tahta):
    if isinstance(tahta[tk[1]][tk[0]][1],Tas.Tas):
        tahta[tk[1]][tk[0]][1].hareket(x,y)
