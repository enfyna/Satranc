def kontrol(s=0,t=0,beyaz=[],siyah=[],ol=0,nl=0): # s -> 0:dikey 1:capraz
                                                  # t -> 0:beyaz 1:siyah
                                                  # t -> 2:piyonlar duz giderken
    tum = list(beyaz+siyah)                       # t -> 3:beyaz piyonlar capraz giderken
                                                  # t -> 4:siyah piyonlar capraz giderken
    nly = nl - nl%10          #nl onlar basamagi 
    oly = ol - ol%10          #ol onlar basamagi
        
    dy = abs(nly-oly)         #onlar basamaklar farkinin mutlak degeri
            
    dx = abs(nl%10 - ol%10)   #birler basamaklarin farkinin mutlak degeri
    
    dxrp = nl%10 - ol%10      #birler basamaklari farki
    
    dyrp = int((nly - oly)/10)#onlar basamaklari farki


    #print(dxrp,dyrp,dx,dy)

    if t == 0:  #Konulacak karede kendi tasimiz var mi?

        for a in range(0,len(beyaz)):
            if beyaz[a] == nl:
                return 0
    elif t == 1:
        for a in range(0,len(siyah)):
            if siyah[a] == nl:
                return 0
    elif t == 2:
        for a in range(0,len(siyah)):
            if siyah[a] == nl or beyaz[a] == nl:
                return 0
    elif t == 3:
        for a in range(0,len(siyah)):
            if siyah[a] == nl :
                return 1
        return 0
    elif t == 4:
        for a in range(0,len(siyah)):
            if beyaz[a] == nl :
                return 1
        return 0
    

    if s == 0 :   #dikey ya da yatay hareketlerde ziplama kontrolu

        if dxrp > 0 and dy ==0:
            for a in range(1,dxrp):
                for b in range(len(tum)):
                    #print(a,ol,ol+a,tum[b],b,dxrp,1)
                    if ol+a == tum[b]:
                        return 0

        elif dxrp < 0 and dy == 0:
            for a in range(-1,dxrp,-1):
                for b in range(len(tum)):
                    #print(a,ol,ol+a,tum[b],b,dxrp,2)
                    if ol+a == tum[b]:
                        return 0

        elif dyrp > 0 and dx ==0:
            for a in range(1,dyrp):
                for b in range(len(tum)):
                    #print(a,ol,ol+a*10,tum[b],b,dxrp,3)
                    if ol+a*10 == tum[b]:
                        return 0

        elif dyrp < 0 and dx == 0:
            for a in range(-1,dyrp,-1):
                for b in range(len(tum)):
                    #print(a,ol,ol+a*10,tum[b],b,dxrp,4)
                    if ol+a*10 == tum[b]:
                        return 0

    if s == 1:  #capraz hareket icin ziplama kontrolu
        #print(dxrp,dyrp)
        if dxrp < 0 and dyrp < 0 :
            for a in range(1,dx):
                for b in range(len(tum)):
                    cl = ol - 11*a
                    if tum[b] == cl:
                        #print(1)
                        return 0

        elif dxrp > 0 and dyrp > 0 :
            for a in range(1,dx):
                for b in range(len(tum)):
                    cl = ol + 11*a
                    if tum[b] == cl:
                        #print(2)
                        return 0
                        
        elif dxrp < 0 and dyrp > 0 :
            for a in range(1,dx):
                for b in range(len(tum)):
                    cl = ol + 9*a
                    #print(a,ol,ol+a*9,tum[b],b,cl,3)
                    if tum[b] == cl:
                        #print(3)
                        return 0
                
        elif dxrp > 0 and dyrp < 0 :
            for a in range(1,dx):
                for b in range(len(tum)):
                    cl = ol - 9*a               
                    if tum[b] == cl:
                        #print(4)
                        return 0

    return 1
