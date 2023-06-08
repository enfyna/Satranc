class Tas:
    posX = 0
    posY = 0
    # Takım 0 == siyah , Takım 1 == beyaz
    takim = 0 
    renk = (0,0,0)
    isim = "isim"
    tahta = []
    def __init__(self,x,y,t,r,i,ta):
        self.posX = x
        self.posY = y
        self.takim = t
        self.renk = r
        self.isim = i
        self.tahta = ta
    def tehdit(self):
        """
        Tahtada hangi karelerin tehdit edildiğini hesaplayan fonksiyon
        """
        pass
    def hareket(self,x,y):
        pass
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
    def __init__(self,x,y,takim,tahta):
        r = (10,10,10) if takim == 0 else (100,100,100)
        super().__init__(x, y,takim,r,"P",tahta)
    def tehdit(self):
         # Piyonun tehdit edebileceği 2 konum var
        for i in range(-1,2,2):
            x = self.posX + i
            y = self.posY + self.takim 
            if self.isinBoard(x, y): # Tehdit ettiği konum tahtanin içindeyse işaretle
                self.isaretle(x, y)
class Kale(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (20,20,20) if takim == 0 else (120,120,120)
        super().__init__(x, y,takim,r,"K",tahta)
    def tehdit(self):
        # Kalenin tehdit ettiği 4 yön var
        for d in [[0,1],[0,-1],[1,0],[-1,0]]: 
            # Bu 4 yönden bir yere çarpasıya kadar 
            # yada tahtadan çıkasıya kadar tehdit et
            x = self.posX
            y = self.posY
            while True:
                x += d[0]
                y += d[1]
                if self.isinBoard(x, y):
                    # Tehdit ettiği konum tahtanin içindeyse işaretle
                    self.isaretle(x, y)
                else:
                    break 
                if isinstance(self.tahta[y][x][1],str):
                    # Tehdit ettiği konumda tas varsa ilerleme
                    break
                 
class Fil(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"F",tahta)
    def tehdit(self):
        # Fil kalenin aynısı sadece çapraz
        for d in [[1,1],[1,-1],[-1,1],[-1,-1]]: 
            # Bu 4 yönden bir yere çarpasıya kadar 
            # yada tahtadan çıkasıya kadar tehdit et
            x = self.posX
            y = self.posY
            while True:
                x += d[0]
                y += d[1]
                if self.isinBoard(x, y):
                    # Tehdit ettiği konum tahtanin içindeyse işaretle
                    self.isaretle(x, y)
                else:
                    break 
                if isinstance(self.tahta[y][x][1],str):
                    # Tehdit ettiği konumda tas varsa ilerleme
                    break
class Kralice(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (50,50,50) if takim == 0 else (150,150,150)
        super().__init__(x, y,takim,r,"Q",tahta)
    def tehdit(self):
        # Kralice kale ve filin toplami
        for d in [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]: 
            # Bu 8 yönden bir yere çarpasıya kadar 
            # yada tahtadan çıkasıya kadar tehdit et
            x = self.posX
            y = self.posY
            while True:
                x += d[0]
                y += d[1]
                if self.isinBoard(x, y):
                    # Tehdit ettiği konum tahtanin içindeyse işaretle
                    self.isaretle(x, y)
                else:
                    break 
                if isinstance(self.tahta[y][x][1],str):
                    # Tehdit ettiği konumda tas varsa ilerleme
                    break
class At(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (30,30,30) if takim == 0 else (130,130,130)
        super().__init__(x, y,takim,r,"A",tahta)
    def tehdit(self):
        # Atin tehdit ettiği 8 tane konum var sirasiyla kontrol edelim 
        for d in [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]: 
            x = self.posX + d[0]
            y = self.posY + d[1]
            if self.isinBoard(x, y):
                # Tehdit ettiği konum tahtanin içindeyse işaretle
                self.isaretle(x, y)

class Kral(Tas):
    def __init__(self,x,y,takim,tahta):
        r = (75,75,75) if takim == 0 else (175,175,175)
        super().__init__(x, y,takim,r,"+",tahta)
    def tehdit(self):
        # Kral kralice gibi ama sadece 1 kare tahdit edebilir
        for d in [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]: 
            x = self.posX + d[0]
            y = self.posY + d[1]
            if self.isinBoard(x, y):
                # Tehdit ettiği konum tahtanin içindeyse işaretle
                self.isaretle(x, y)
