class Tas:
    posX  : int
    posY  : int
    isim  : str
    renk  : tuple
    takim : int
    tahta : list
    yasiyor : bool = True
    def __init__(self,x,y,t,r,i,ta):
        self.posX, self.posY = x, y
        self.takim = t
        self.renk  = r
        self.isim  = i
        self.tahta = ta
    def tehdit(self):
        for x,y in self.gidebilecegi_yerler():
            self.isaretle(x, y)
    def hareket(self,x,y):
        if self.isinBoard(x, y):
            if isinstance(self.tahta[y][x][1],Tas):
                self.tahta[y][x][1].yasiyor = False
            self.posX = x
            self.posY = y
    def gidebilirYon(self,yon,mesafe = 9,piyonduz = False,piyoncapraz = False,kral = False):
        konumlar = []
        for d in yon:
            x = self.posX
            y = self.posY
            for _ in range(mesafe):
                x += d[0]
                y += d[1]
                if not self.isinBoard(x, y):
                    #tahta dışına çıktık devam etmeye gerek yok
                    break
                if isinstance(self.tahta[y][x][1],Tas):
                    # Gidilebilen konumda tas varsa tasin karsi takimdan olmasi lazim
                    # Piyon hariç piyon herhangi bir taş varsa ilerleyemez
                    if self.tahta[y][x][1].takim != self.takim and not piyonduz:
                        konumlar.append([x,y])
                    break
                if not piyoncapraz and not kral:
                    # Piyon değilsek ve konumda tas yoksa gidebiliriz
                    konumlar.append([x,y])
                elif kral:
                    if self.tahta[y][x][0] == None:
                        konumlar.append([x,y])
                        continue
                    # Kral tehdit edilen yerlere gidemez
                    if self.tahta[y][x][0] == 0 or self.tahta[y][x][0] != self.takim:
                        continue
                    konumlar.append([x,y])
        return konumlar
    def isaretle(self,x,y):
        if self.tahta[y][x][0] == None:
            self.tahta[y][x][0] = self.takim
        elif self.tahta[y][x][0] == self.takim:
            return
        else:
            self.tahta[y][x][0] = 0
    def isinBoard(self,x,y):
        """Verilen koordinat tahtanın içinde mi"""
        return max(0,min(7,x)) == x and max(0,min(7,y)) == y
    def __repr__(self):
        return self.isim
    pass

class Piyon(Tas):
    ilkhareket = True
    def __init__(self,x,y,takim,tahta):
        r = (10,10,10) if takim == 0 else (100,100,100)
        super().__init__(x, y,takim,r,"P",tahta)
    def gidebilecegi_yerler(self):
        # Normal durumda piyon 1 kare ilerleyebilir
        # İlk defa hereket ediliyorsa 2 kare ilerleyebilir
        # caprazinda dusman varsa capraz da gidebilir
        u = 2 if self.ilkhareket else 1

        return  self.gidebilirYon(
            [[0,self.takim]],u,piyonduz=True # Dikey 1 veya 2 konum gidebilir
            ) + self.gidebilirYon(
            [[-1,self.takim],[1,self.takim]],1,piyoncapraz=True # Caprazinda dusman varsa gidebilir
            )
    def tehdit(self):
        # Piyonun tehdit edebileceği 2 konum var
        for x,y in self.gidebilirYon([[-1,int(self.takim)],[1,int(self.takim)]],1):
            self.isaretle(x, y)

class At(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"A",tahta)
        return
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]],1)

class Kale(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (20,20,20) if takim == 0 else (120,120,120)
        super().__init__(x, y,takim,r,"K",tahta)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[0,1],[0,-1],[1,0],[-1,0]])

class Fil(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"F",tahta)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1]])

class Vezir(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (50,50,50) if takim == 0 else (150,150,150)
        super().__init__(x, y,takim,r,"V",tahta)
        return
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]])

class Şah(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (75,75,75) if takim == 0 else (175,175,175)
        super().__init__(x, y,takim,r,"Ş",tahta)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]],1,kral=True)
