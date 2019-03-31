import random
from rantex import vibor, sravnapovtor

kolslow =1
colbukv =1
colslenter = True
sdvigtochki = False
tochka = True
zpt = 0
vestext = 1000
nomerslova = 0
colslpred = 0
abzats = 0
predlinabzats = 0
abzy = True



while kolslow < vestext:
    zptline = []
    if  colslenter == True:
        colslpred = int(random.randint(6,12))
        if sdvigtochki == True:
            sdvigtochki = False
        else:
            colslenter = False


        if tochka == True:
            ciklezpt = 3
            skolzpt = 1
            gdezpt = 0
            gdezptto = 1
            while ciklezpt <= colslpred and ciklezpt > 0:
                gdezpt = 0
                gdezpt = int(random.randint(2, colslpred))
                #print(ciklezpt, gdezpt,'x')

                if zptline.count(gdezpt) == 1:
                    ciklezpt -= 3
                    #print('xxxx')

                else:
                    ciklezpt += 3
                    zptline.append(gdezpt)
                    #gdezptto = gdezpt

                    #zptline.append(gdezpt)
                gdezptto += 1
                if gdezptto == 5:
                    break
            sortozptline = sorted(zptline)
            #print(sortozptline)


    nomerslova += 1
    colslpred -= 1
    if colslpred == 1:
        colslenter = True
    if abzy == True:
        predlinabzats = int(random.randint(20,50))

        abzy = False
    if tochka == True:
        abzats += 1
        #print(abzats, predlinabzats)
    colbutoo = colbukv
    if colbutoo == 1:
        colbukv = int(random.randint(2,7))
    elif colbutoo == 2:
        colbukv = int(random.randint(3, 7))
    else:
        colbukv = int(random.randint(1, 7))

    if colbukv == 2:
        listtwolet = ['an','is','to','on','it','in','if','as','at','of','or','so']
        wordtwolet = random.choice(listtwolet)
        if tochka == True:
            print(wordtwolet.title(), end='')
        else:
            print (wordtwolet, end='')
    elif colbukv == 1:
        if tochka == True:
            print('A', end='')
        else:
            print ('a', end='')
    else:
        randomfirstbukv =''
        randomsecbukv = ''
        randomsravbuk = ''
        sravnapovtory = False
        for slogstep in range(colbukv):
            slogstep += 1
            #randomsecbukv = ''
            #slogstep += 1
            spisokbukv = ('qwertyuiopasdfghjklzxcvbnm')

            if slogstep == 1:
                randomfirstbukv = random.choice(spisokbukv)
                #sravnapovtory = sravnapovtor(randomsecbukv,randomfirstbukv,sravnapovtory)
                randomsravbuk = randomfirstbukv
                randomsecbukv = randomfirstbukv
            elif slogstep == 2:
                iterra = vibor(randomfirstbukv, randomsecbukv)
                randomfirstbukv = iterra[0]
                randomsecbukv = iterra [1]
                randomsravbuk = randomfirstbukv
            elif slogstep == 3:
                randomfirstbukv = random.choice ('eyuioa')
                sravnapovtory = sravnapovtor(randomsecbukv, randomfirstbukv, sravnapovtory)
                randomsecbukv = randomfirstbukv

                
            elif slogstep == 4:
                iterra = vibor(randomfirstbukv, randomsravbuk)
                randomfirstbukv = iterra[0]
                randomsravbuk = iterra[1]
                sravnapovtory = sravnapovtor(randomsecbukv, randomfirstbukv, sravnapovtory)
                randomsecbukv = randomfirstbukv
            elif slogstep == 5:
                randomfirstbukv = random.choice('qwrtpsdfghjklzxcvbnm')
                sravnapovtory = sravnapovtor(randomsecbukv, randomfirstbukv, sravnapovtory)
                randomsecbukv = randomfirstbukv
            elif slogstep == 6:
                iterra = vibor(randomfirstbukv, randomsravbuk)
                randomfirstbukv = iterra[0]
                randomsravbuk = iterra[1]
                sravnapovtory = sravnapovtor(randomsecbukv, randomfirstbukv, sravnapovtory)
                randomsecbukv = randomfirstbukv
            else:
                if randomfirstbukv in ('eyuioa'):
                    randomfirstbukv = random.choice('qwrtpsdfghjklzxcvbnm')
                    randomsecbukv = randomfirstbukv
                else:
                    randomfirstbukv = random.choice('eyuioa')
                    randomsecbukv = randomfirstbukv
            if slogstep == 1 and tochka == True:
                randomsecbukv = randomsecbukv.title()
            if sravnapovtory == False:
                print (randomsecbukv, end='')
            else:
                slogstep -=1

    if colslenter == True:
        if colbukv < 3:
            sdvigtochki = True
            print(' ', end='')
        else:
            if predlinabzats == abzats:
                print('.')
                print('    ', end='')
                abzy = True
                abzats = 0
            else:
                print('. ', end='')
            sdvigtochki = False
            tochka = True

    else:
        #nomerzpt = 0
        #for nomerzpt in sortozptline:
        if colslpred in sortozptline and colbukv > 2:
            print(', ', end='')
        else:
            print(' ', end='')
        tochka = False










    kolslow +=1

