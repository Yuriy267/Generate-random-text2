import  random
def vibor(a, c):
    if a in ('eyuioa'):
        a = random.choice('qwrtpsdfghjklzxcvbnm')

        c = a
    else:
        a = random.choice('eyuioa')

        c = a


    return [a,c]

def sravnapovtor(b,d,e):
    e = False
    if b == d:
        e = True
    return e