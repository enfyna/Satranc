class Tas:
    posX  : int
    posY  : int
    isim  : str
    takim : int
    tahta : list
    renk : tuple
    font_krt : str
    yasiyor : bool = True
    def __init__(self,x,y,t,i,ta,f):
        self.posX, self.posY = x, y
        self.takim = t
        self.isim  = i
        self.tahta = ta
        self.font_krt = f
    def tehdit(self):
        for x,y in self.gidebilecegi_yerler():
            self.isaretle(x, y)
    def hareket(self,x,y):
        if self.isinBoard(x, y):
            if isinstance(self.tahta[y][x][1],Tas):
                # Hareket ettiğimiz konumda taş varsa
                # Taşı öldür
                self.tahta[y][x][1].yasiyor = False
            self.posX, self.posY = x, y
            if isinstance(self, Piyon):
                # Hareket ettirilen taş piyon ise
                # İlk hareketimizi kullanmış olduk
                self.ilkhareket = False
    def gidebilirYon(self,yon,mesafe = 9,piyonduz = False,piyoncapraz = False,kral = False):
        konumlar = []
        for d in yon:
            x, y = self.posX, self.posY
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
        return 0 <= x <= 7 and 0 <= y <= 7
    def __repr__(self):
        return self.isim
    pass

class Piyon(Tas):
    ilkhareket = True
    def __init__(self,x,y,takim,tahta):
        f = "o" 
        super().__init__(x, y,takim,"P",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
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
        f = "m" 
        super().__init__(x, y,takim,"A",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
        return
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]],1)

class Kale(Tas):
    def __init__(self,x,y,takim,tahta):
        f = "t"
        super().__init__(x, y,takim,"K",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[0,1],[0,-1],[1,0],[-1,0]])

class Fil(Tas):
    def __init__(self,x,y,takim,tahta):
        f = "v"
        super().__init__(x, y,takim,"F",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1]])

class Vezir(Tas):
    def __init__(self,x,y,takim,tahta):
        f = "w"
        super().__init__(x, y,takim,"V",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
        return
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]])

class Şah(Tas):
    def __init__(self,x,y,takim,tahta):
        f = "l"
        super().__init__(x, y,takim,"Ş",tahta,f)
        self.renk = (220,220,220) if takim == 1 else (0,0,0)
    def gidebilecegi_yerler(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]],1,kral=True)
