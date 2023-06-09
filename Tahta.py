import Tas

def oyunuBaslat():
    tahta = [[[None,0] for _ in range(8)] for _ in range(8)]
    # None -> o karede tehdit var mı onu kaydediyor 
    # Mesela 1e esit ise beyaz o kareyi tehdit ediyor.
    # ---
    # 0 -> ise o karede bulunan taşı kaydediyor
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

    taslar.append(Tas.Kral(4, 7, -1, tahta))
    taslar.append(Tas.Kralice(3, 7, -1, tahta))

    taslar.append(Tas.Kral(4, 0, 1, tahta))
    taslar.append(Tas.Kralice(3, 0, 1, tahta))

    return tahta , taslar

def tahtaGuncelle(tahta , taslar):
    for i in range(len(tahta)): # tahtayi sifirla
        for j in range(len(tahta)):
            tahta[i][j][0] = None
            tahta[i][j][1] = 0
    
    for i in taslar: # Taslari diz
        tahta[i.posY][i.posX][1] = i

    for i in taslar: # Taslarin tehditlerini hesapla
        i.tehdit()

    return taslar

def yazdir(tahta , taslar):
    print("\n")
    for i in range(7,-1,-1):
        print(i+1,end=" - ")    
        for j in range(8):
            print(tahta[i][j][1],end=" ")
        print("")
    print("    ",end="")
    for i in range(8):
        print("|",end=" ")
    print("\n    ",end="")
    for i in ["A","B","C","D","E","F","G","H"]:
        print(i,end=" ")
    print("\n")

def gidebilir(x,y,tahta):
    if isinstance(tahta[y][x][1],Tas.Tas):
        return tahta[y][x][1].gidebilir()
    return []

if __name__ == "__main__":
    tahta , taslar = oyunuBaslat()
    tahtaGuncelle(tahta , taslar)
    yazdir(tahta , taslar)
    
