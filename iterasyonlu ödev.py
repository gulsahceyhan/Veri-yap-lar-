
def uzunluk_çizimi(lenght,deger=' '):
    çizim='-'*int(lenght)+deger
    print(çizim)
  
def içi(k,merkez):
    print(k*'-')
    print((k+1)*'-')
    print(k*'-')
    print(merkez*'-')
    print(k*'-')
    print((k+1)*'-')
    print(k*'-')

def hepsi(lenght,k):
    uzunluk_çizimi(lenght,'0')
    merkez=lenght-1
    k=lenght-merkez
    for i in range(1,3):
        içi(k,merkez)
        uzunluk_çizimi(lenght,str(i))
    
hepsi(4,2)
print("========================================")

def uzunluk_çizimi2(lenght2,deger2=' '):
    çizim2='-'*int(lenght2)+deger2
    print(çizim2)
    
def içi2(k2):
    print(k2*'-')
    print((k2+1)*'-')
    print(k2*'-')

def hepsi2(lenght2,k2):
    k2=lenght2-2
    uzunluk_çizimi2(lenght2,'0')
    for i in range(1,4):
        içi2(k2)
        uzunluk_çizimi2(lenght2,str(i))

hepsi2(3,3)
print("=========================================")

def uzunluk_çizimi3(lenght3,deger3=' '):
    çizim3='-'*int(lenght3)+deger3
    print(çizim3)
    
def içi3(k3,m):
    print(k3*'-')
    print((k3+1)*'-')
    print(k3*'-')
    print((m-1)*'-')
    print(k3*'-')
    print((k3+1)*'-')
    print(k3*'-')
    print(m*'-')
    print(k3*'-')
    print((k3+1)*'-')
    print(k3*'-')
    print((m-1)*'-')
    print(k3*'-')
    print((k3+1)*'-')
    print(k3*'-')
    
def hepsi3(lenght3,k3):
    uzunluk_çizimi3(lenght3,'0')
    m=int(lenght3)-1
    k3=lenght3-m
    for i in range(1,2):
        içi3(k3,m)
        uzunluk_çizimi3(lenght3,str(i))

hepsi3(5,3)
print("====================================")
    












