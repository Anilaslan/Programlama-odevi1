##1.BÖLÜM##

def gelir():
    x=int(input("Finansman gelirini giriniz:"))
    y=int(input("Pazar gelirini giriniz:"))
    z=int(input("kira gelirini giriniz:"))
    gelir=x+y+z
    return gelir

def gider():
    a=int(input("Ücreti giriniz:"))
    b=int(input("Finansman giderini giriniz:"))
    c=int(input("Pazar giderini giriniz:"))
    d=int(input("Kira giderini giriniz"))
    e=int(input("Muhasebe giderini giriniz:"))
    gider=a+b+c+d+e
    return gider

p=gelir()
g=gider()

kar=p-g

if kar>1000:
    print("Şirket kâr elde etmiştir")
else:
    print("Şirket zarar etmiştir")


##2.BÖLÜM##

def kullanilabilirlik():
    planlanmisUretimSuresi=int(input("Planlanmış üretim süresini giriniz:"))
    plansizDurus=int(input("Plansız duruşu giriniz:"))
    kullanilabilirlik=(planlanmisUretimSuresi-plansizDurus)/planlanmisUretimSuresi
    global deneme
    deneme=(planlanmisUretimSuresi-plansizDurus)
    return kullanilabilirlik
    
def performans():
    standartCevrimZamani=int(input("Standart çevrim zamanını giriniz:"))
    uretimMiktari=int(input("Üretim miktarını giriniz:"))
    performans=(standartCevrimZamani*uretimMiktari)/deneme
    return performans

def kalite():
    saglamUrunMiktari=int(input("Sağlam ürün miktarını giriniz:"))
    toplamUretimMiktari=int(input("Toplam üretim miktarını giriniz:"))
    kalite=saglamUrunMiktari/toplamUretimMiktari
    return kalite


a=kullanilabilirlik()
b=performans()
c=kalite()

oee=a*b*c*100
print("%",oee)

##3.BÖLÜM##

def abc():
    q=int(input("satış miktarını giriniz:"))
    w=int(input("Birim satış fiyatını giriniz:"))
    ciro=q*w
    abc=ciro/25
    return abc
v=abc()
print(v)
  
        


