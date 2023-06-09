class Tas:
    posX : int
    posY : int
    takim : int
    renk : tuple
    isim : str
    tahta : list
    def __init__(self,x,y,t,r,i,ta):
        self.posX = x
        self.posY = y
        self.takim = t
        self.renk = r
        self.isim = i
        self.tahta = ta
    def tehdit(self):
        for x,y in self.gidebilir():
            self.isaretle(x, y)
        return
    def hareket(self,x,y):
        pass
    def gidebilirYon(self,yon,mesafe = 9):
        konumlar = []
        for d in yon:
            x = self.posX
            y = self.posY
            for _ in range(mesafe):
                x += d[0]
                y += d[1]
                if not self.isinBoard(x, y):
                    #tahta dışına çıktık
                    break
                if isinstance(self.tahta[y][x][1],Tas):
                    # Gidilebilen konumda tas varsa tasin karsi takimdan olmasi lazim
                    if self.tahta[y][x][1].takim != self.takim:
                        konumlar.append([x,y])
                    break
                konumlar.append([x,y])
        return konumlar
    def isaretle(self,x,y):
        if self.tahta[y][x][0] == None:
            self.tahta[y][x][0] = self.takim
        elif self.tahta[y][x][0] == self.takim:
            return
        else:
            self.tahta[y][x][0] = 0
        return
    def isinBoard(self,x,y):
        """Verilen koordinat tahtanın içinde mi"""
        if max(0,min(7,x)) != x or max(0,min(7,y)) != y:
            return False
        return True
    def __repr__(self):
        return self.isim
    pass

class Piyon(Tas):
    ilkhareket = True
    def __init__(self,x,y,takim,tahta):
        r = (10,10,10) if takim == 0 else (100,100,100)
        super().__init__(x, y,takim,r,"P",tahta)
    def gidebilir(self):
        # Normal durumda piyonun gidebileceği tek bir konum var
        # İlk defa hereket ediliyorsa 2 konum var
        # caprazinda dusman varsa capraz da gidebilir
        konumlar = []
        u = 2 if self.ilkhareket else 1
        for i in range(1,1+u):
            y = self.posY + (self.takim*i)
            x = self.posX
            if not self.isinBoard(x, y):
                continue
            if not isinstance(self.tahta[y][x][1],Tas):
                # Gidilebilen konumda tas yoksa sorun yok
                konumlar.append([x,y])
                continue
            elif isinstance(self.tahta[y][x][1],Tas):
                # Gidilebilen konumda tas varsa piyon ilerleyemez
                break
        for i in range(-1,2,2):
            y = self.posY + (self.takim)
            x = self.posX + i
            if not self.isinBoard(x, y):
                continue
            if isinstance(self.tahta[y][x][1],Tas) and self.tahta[y][x][1].takim != self.takim:
                # Gidilebilen konumda dusman tas varsa piyon capraz gidebilir
                konumlar.append([x,y])
        return konumlar
    def tehdit(self):
        # Piyonun tehdit edebileceği 2 konum var
        for i in range(-1,2,2):
            x = self.posX + i
            y = self.posY + self.takim
            if self.isinBoard(x, y): # Tehdit ettiği konum tahtanin içindeyse işaretle
                self.isaretle(x, y)

class At(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"A",tahta)
        return
    def gidebilir(self):
        return self.gidebilirYon([[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]],1)

class Kale(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (20,20,20) if takim == 0 else (120,120,120)
        super().__init__(x, y,takim,r,"K",tahta)
    def gidebilir(self):
        return self.gidebilirYon([[0,1],[0,-1],[1,0],[-1,0]])

class Fil(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"F",tahta)
    def gidebilir(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1]])

class Kralice(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (50,50,50) if takim == 0 else (150,150,150)
        super().__init__(x, y,takim,r,"Q",tahta)
        return
    def gidebilir(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]])
        
class Kral(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (75,75,75) if takim == 0 else (175,175,175)
        super().__init__(x, y,takim,r,"+",tahta)
    def gidebilir(self):
        return self.gidebilirYon([[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]],1)
