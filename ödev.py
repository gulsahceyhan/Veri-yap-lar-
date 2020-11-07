#3 fonksiyon olucak
#biri ortayı çizdircek
#diğeri büyük tick uzunluğunu yazdırcak sadece ve karşısın gelen sayıyı.atıyorum 2 uzunlugundaysa 0 1 2 diye.
#ben forla bu fonksiyonları çağırıcam
#sonrada bu çağırdığımı yazdırıcam
#lenght=4 inç =2



def uzunluk_çizimi(lenght,deger=' '):
    çizim='-'*int(lenght)+deger
    print(çizim)
    
def recursive(meruzunluk):
    if meruzunluk>0:
       recursive(meruzunluk-1)
       uzunluk_çizimi(meruzunluk)
       recursive(meruzunluk-1)

def hepsini_yazdırma(inç,lenght):
    for i in range (1,inç+1):
        recursive(lenght-1)
        uzunluk_çizimi(lenght,str(i))

while True:
   print("inç değerini giriniz:")
   inç1=int(input())
   print("lenght değerini giriniz:")
   lenght1=int(input())
   print(str(inç1)+" inç uzunuluğundaki cetveliniz: \n")
   uzunluk_çizimi(lenght1,'0')
   hepsini_yazdırma(inç1,lenght1)
   print("bitti")
   
  
