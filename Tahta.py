import Tas

tahta = [[[None,0] for _ in range(8)] for _ in range(8)]
# None o karede tehdit var mı onu kaydediyor 
# Mesela 1e esit ise beyaz o kareyi tehdit ediyor.
# 0 ise o karede bulunan taşı kaydediyor
taslar = []

def oyunuBaslat():
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

    taslar.append(Tas.Kral(3, 7, -1, tahta))
    taslar.append(Tas.Kralice(4, 7, -1, tahta))

    taslar.append(Tas.Kral(3, 0, 1, tahta))
    taslar.append(Tas.Kralice(4, 0, 1, tahta))

def tahtaGuncelle():
    # Tahtayı sıfırla
    tahta = [[[None,0] for _ in range(8)] for _ in range(8)]

    for i in taslar: # Taslari diz
        tahta[i.posY][i.posX][1] = str(i)

    for i in taslar: # Taslarin tehditlerini hesapla
        i.tehdit()

    return taslar

def yazdir():
    for i in range(7,-1,-1): 
        print(i,end=" ")
        print(tahta[i])

if __name__ == "__main__":
    oyunuBaslat()
    tahtaGuncelle()
    yazdir()