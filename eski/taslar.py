import atlama


beyaz = []
siyah = []


def bt(s=0,x=0,y=0): # s -> 0:sifirdan diz                          
                     # s -> 1:tahta icin konum gonder
                     # s -> 2:sil
                     # s -> 3:hareket et
                     # s -> 4:kral hayatta mi kontrol et

                     # x = nl , y = ol
    

    if s == 0:
        beyaz.clear()
                         #listedeki siralari :
        beyaz.append(15) #kral            > 0
        beyaz.append(14) #kralice         > 1
        beyaz.append(17) #at              > 2
        beyaz.append(12) #at2             > 3
        beyaz.append(16) #fil             > 4 
        beyaz.append(13) #fil2            > 5
        beyaz.append(11) #kale            > 6
        beyaz.append(18) #kale2           > 7 
        for a in range(8,16):   #piyonlar > 8 ... 15
            beyaz.append(a+13)
            #beyaz.append(0)
                           
        return beyaz

    elif s == 1:
        for a in range(0,16):
            if beyaz[a] == 10*x+y and a == 0 :
                return 1
            if beyaz[a] == 10*x+y and a == 1 :
                return 2
            if beyaz[a] == 10*x+y and ( a == 2 or a == 3 ) :
                return 3
            if beyaz[a] == 10*x+y and ( a == 4 or a == 5 ) :
                return 4
            if beyaz[a] == 10*x+y and ( a == 6 or a == 7 ) :
                return 5
            if beyaz[a] == 10*x+y and a >= 8 :
                return 6

    elif s == 2:
        for a in range(0,16):
            if  beyaz[a] == x :
                beyaz[a] = 0
                return 0
        return 0
    
    elif s == 3:      
        t = 0 #hareket eden tas var mı ?
        nl = x
        ol = y

        nly = nl - nl%10          #nl onlar basamagi 
        oly = ol - ol%10          #ol onlar basamagi
        
        dy = abs(nly-oly)         #onlar basamaklar farkinin mutlak degeri
                
        dx = abs(nl%10 - ol%10)   #birler basamaklarin farkinin mutlak degeri
        
        dxrp = nl%10 - ol%10      #birler basamaklari farki
        
        dyrp = int((nly - oly)/10)#onlar basamaklari farki

        #print(dxrp,dyrp,dx,dy)
        
        for a in range(0,16):
            if  beyaz[a] == ol :
                h = a #hareket eden tas var ama hareketi dogru mu ?
                t = 1

        if t == 0:
            return 0
        
        if t == 1:        
            if h == 2 or h == 3 : #At ise

                d = nl - ol #at icin basitce konum farki 

                if d == 8 or d == 12 or d ==19 or d == 21 or d == -8 or d == -12 or d == -21 or d == -19:
                    if atlama.kontrol(2,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                
            elif h >= 8 :          #Piyon ise
                if (dxrp == 0) and (dy == 10) and (dyrp == 1): #duz giderken
                    if atlama.kontrol(0,2,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif (dyrp == 1) and (dx == 1):                 #capraz giderken
                    if atlama.kontrol(1,3,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif (dxrp == 0) and (dy == 20) and (dyrp == 2) and (oly == 20): #ilk defa hareket ediyorsa çift kare ilerleyebilir
                    if atlama.kontrol(0,2,beyaz,siyah,ol,nl)==1: #piyon geri gidemedigi icin eger baslangıc noktasindaysa hareket etmemistir
                        beyaz[h] = nl
                        return 1
                    
            elif h == 4 or h == 5: #Fil ise
                if (dx < 0 or dx > 0) and (dy > 0 or dy < 0) and ( (dy/10) == dx):
                    if atlama.kontrol(1,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                
            elif h == 6 or h == 7: #Kale ise
                if (dx == 0) and (dy > 0 or dy < 0):
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif (dy == 0) and (dx > 0 or dx < 0):
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1

            elif h == 1:            #Kralice ise
                if (dx < 0 or dx > 0) and (dy > 0 or dy < 0) and ( (dy/10) == dx):
                    if atlama.kontrol(1,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif (dx == 0) and (dy > 0 or dy < 0):
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif (dy == 0) and (dx > 0 or dx < 0):
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1

            elif h == 0:            #Kral ise
                if dx <= 1 and dy/10 <= 1: #normal hereketinde her yone tek kare ilerleyebilir
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        return 1
                elif dxrp == 2 and dy == 0 and beyaz[7]==18 and beyaz[0]==15: #rok atarken 2 kare ilerler 
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:              #kalede 2 kare ilerler
                        beyaz[h] = nl 
                        beyaz[7] = 16 #eger kral 2 kare ilerleyebiliyorsa ortasi bostur yani kale icin hesap yapmamıza gerek yok
                        return 1
                elif dxrp == -3 and dy == 0 and beyaz[6]==11 and beyaz[0]==15:
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        beyaz[h] = nl
                        beyaz[6] = 14
                        return 1

            return 0

    elif s == 4:
        x = beyaz[0]
        return x

    return None
        
#################################################################################################################################################################################    
#################################################################################################################################################################################
#################################################################################################################################################################################

                
def st(s=0,x=0,y=0): # s -> 0:sifirdan diz                          
                     # s -> 1:tahta icin konum gonder
                     # s -> 2:sil
                     # s -> 3:hareket et
                     # s -> 4:kral hayatta mi kontrol et

                     # x = nl , y = ol
    

    if s == 0:
        siyah.clear()
                         #listedeki siralari :
        siyah.append(85) #kral            > 0
        siyah.append(84) #kralice         > 1
        siyah.append(87) #at              > 2
        siyah.append(82) #at2             > 3
        siyah.append(86) #fil             > 4 
        siyah.append(83) #fil2            > 5
        siyah.append(81) #kale            > 6
        siyah.append(88) #kale2           > 7 
        for a in range(8,16):   #piyonlar > 8 ... 15
            siyah.append(a+63)  
            #siyah.append(0)           
        return siyah

    elif s == 1:
        for a in range(0,16):
            if siyah[a] == 10*x+y and a == 0 :
                return 7
            if siyah[a] == 10*x+y and a == 1 :
                return 8
            if siyah[a] == 10*x+y and ( a == 2 or a == 3 ) :
                return 9
            if siyah[a] == 10*x+y and ( a == 4 or a == 5 ) :
                return 10
            if siyah[a] == 10*x+y and ( a == 6 or a == 7 ) :
                return 11
            if siyah[a] == 10*x+y and a >= 8 :
                return 12

    elif s == 2:
        for a in range(0,16):
            if  siyah[a] == x :
                siyah[a] = 0
                return 0
        return 0
    
    elif s == 3:      
        t = 0 #hareket eden tas var mı ?
        nl = x
        ol = y

        nly = nl - nl%10          #nl onlar basamagi 
        oly = ol - ol%10          #ol onlar basamagi
        
        dy = abs(nly-oly)         #onlar basamaklar farkinin mutlak degeri
                
        dx = abs(nl%10 - ol%10)   #birler basamaklarin farkinin mutlak degeri
        
        dxrp = nl%10 - ol%10      #birler basamaklari farki
        
        dyrp = int((nly - oly)/10)#onlar basamaklari farki

        #print(dxrp,dyrp,dy,dx,nly,oly,d)
        
        for a in range(0,16):
            if  siyah[a] == ol :
                h = a #hareket eden tas var ama hareketi dogru mu ?
                t = 1
            

        if t == 0:
            return 0
        
        if t == 1:        
            if h == 2 or h == 3 :  #At ise

                d = nl - ol 
                
                if d == 8 or d == 12 or d ==19 or d == 21 or d == -8 or d == -12 or d == -21 or d == -19:
                    if atlama.kontrol(2,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                
            elif h >= 8 :          #Piyon ise
                if (dxrp == 0) and (dy == 10) and (dyrp == -1):
                    if atlama.kontrol(0,2,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif (dyrp == -1) and (dx == 1):
                    if atlama.kontrol(1,4,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif (dxrp == 0) and (dy == 20) and (dyrp == -2) and (oly == 70):
                    if atlama.kontrol(0,2,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                    
            elif h == 4 or h == 5: #Fil ise
                if (dx < 0 or dx > 0) and (dy > 0 or dy < 0) and ( (dy/10) == dx):
                    if atlama.kontrol(1,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                    
            elif h == 6 or h == 7: #Kale ise
                if (dx == 0) and (dy > 0 or dy < 0):
                    if atlama.kontrol(0,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif (dy == 0) and (dx > 0 or dx < 0):
                    if atlama.kontrol(0,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1

            elif h == 1:            #Kralice ise
                if (dx < 0 or dx > 0) and (dy > 0 or dy < 0) and ( (dy/10) == dx):
                    if atlama.kontrol(1,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif (dx == 0) and (dy > 0 or dy < 0):
                    if atlama.kontrol(0,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif (dy == 0) and (dx > 0 or dx < 0):
                    if atlama.kontrol(0,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1

            elif h == 0:            #Kral ise
                if (dx <= 1) or (dy <= 1):
                    if atlama.kontrol(0,1,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        return 1
                elif dxrp == 2 and dy == 0 and siyah[7]==81 and siyah[0]==85:
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        siyah[7] = 86
                        return 1
                elif dxrp == -3 and dy == 0 and siyah[6]==88 and siyah[0]==85:
                    if atlama.kontrol(0,0,beyaz,siyah,ol,nl)==1:
                        siyah[h] = nl
                        siyah[6] = 84
                        return 1
                
            return 0

    elif s == 4:
        x = siyah[0]
        return x


    return None
        
    

