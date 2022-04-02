import taslar

taslar.bt()
taslar.st()

sira = 0

while taslar.bt(4) != 0 and taslar.st(4) != 0:


    for y in range(1,9):

        if y == 1:
            print("╔══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╦══════════╗")
        else:
            print("╠══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╬══════════╣")

        if y%2 == 1 :
            print("║██████████║          ║██████████║          ║██████████║          ║██████████║          ║")
        else:
            print("║          ║██████████║          ║██████████║          ║██████████║          ║██████████║")
            
        for x in range(1,9):
            if   taslar.bt(1,x,y)==1:
                print("║  #kral   ",end = "")
            elif taslar.bt(1,x,y)==2:
                print("║ #kralice ",end = "")
            elif taslar.bt(1,x,y)==3:
                print("║   #at    ",end = "")
            elif taslar.bt(1,x,y)==4:
                print("║  #fil    ",end = "")
            elif taslar.bt(1,x,y)==5:
                print("║  #kale   ",end = "")
            elif taslar.bt(1,x,y)==6:
                print("║  #piyon  ",end = "")
            elif taslar.st(1,x,y)==7:
                print("║   kral   ",end = "")
            elif taslar.st(1,x,y)==8:
                print("║  kralice ",end = "")
            elif taslar.st(1,x,y)==9:
                print("║    at    ",end = "")
            elif taslar.st(1,x,y)==10:
                print("║   fil    ",end = "")
            elif taslar.st(1,x,y)==11:
                print("║   kale   ",end = "")
            elif taslar.st(1,x,y)==12:
                print("║   piyon  ",end = "")
            elif (x+y)%2 == 0:
                print("║██████████",end = "")
            else:
                print("║          ",end = "")
        #print("\n")

        if y%2 == 1 :
            print("║\n║████████{}{}║        {}{}║████████{}{}║        {}{}║████████{}{}║        {}{}║████████{}{}║        {}{}║".format(x-7,y,x-6,y,x-5,y,x-4,y,x-3,y,x-2,y,x-1,y,x,y))
        else:
            print("║\n║        {}{}║████████{}{}║        {}{}║████████{}{}║        {}{}║████████{}{}║        {}{}║████████{}{}║".format(x-7,y,x-6,y,x-5,y,x-4,y,x-3,y,x-2,y,x-1,y,x,y)  )
        
        if y == 8:
            print("╚══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╩══════════╝\n\n\n\n")
        #print("\n")
        

    #print("beyaz taslar:",end = "")
    #print(b)
        
    #print("siyah taslar:",end = "")
    #print(s)
    
    v = 0

    if sira%2 == 0 :
        while v == 0:
            
            print("Sira Beyazda")

            print("Oynamak istediginiz tasin konumu : ",end = "")
            ol = int(input())
            print("Nereye gitmek istiyorsun : ",end = "")
            nl = int(input())
            
            if ol<11 or ol> 88 or nl<11 or nl>88 or  nl%10==9 or nl%10==0 or ol%10==9 or ol%10==0:
                print("Hatali konum,tahtanin icinde bir konum yazin!")
            else:
                v = taslar.bt(3,nl,ol)
                if v == 0 :
                    print("Hatali Hamle!")
                elif v == 1:
                    taslar.st(2,nl)
                    sira+=1

    else:
        while v == 0:
            
            print("Sira Siyahta")

            print("Oynamak istediginiz tasin konumu : ",end = "")
            ol = int(input())
            print("Nereye gitmek istiyorsun : ",end = "")
            nl = int(input())
            
            if ol<11 or ol> 88 or nl<11 or nl>88 or  nl%10==9 or nl%10==0 or ol%10==9 or ol%10==0:
                print("Hatali konum,tahtanin icinde bir konum yazin!")
            else:
                v = taslar.st(3,nl,ol)
                if v == 0 :
                    print("Hatali Hamle!")
                elif v == 1:
                    taslar.bt(2,nl)
                    sira+=1


    print("\n\n\n\n\n\n\n\n")


if taslar.bt(4) == 0:
    print("SİYAH KAZANDİ!")
else:
    print("BEYAZ KAZANDİ!")



















