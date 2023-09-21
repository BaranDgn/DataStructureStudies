# Memoization - Dinamik programlama

# Hesaplama yaptıgımızda bir sonucu dogru gitmeye calısıyorken
# o hesaplamayı tekrar tekrar yapmak zorunda kalabilir.
# Bu agaclarla ilgili de olabilir baska bir seyi ile ilgili de olabilir.

# mesela agac uzerinde bir veri aradıgımızı dusunelim.
# veriyi ararken devamlı aynı node ların uzerinde dolastıgımızı farkedebiliriz.
# Halbuki daha önce gectigimiz node ları bir yere kaydetsek
# ve sonucun o olmadıgını bilirsek bir daha onların üzerimnde gecmek zorunda kalmayız.

# Özetle; Bir algorithm kurarak sonuca gitmeye calısırken
# daha önce hesapladıgınız durumların tekrar tekrar üzerinde
# geçilmesi gerekiyorsa bunları kaydedersek bir yere çok daha dinamik bir programlama yapmış oluruz.

# timeit --> kucuk kodların execution time ını gosterir. mesela bir fonksiyonun kaç milisaniye calısacagını gosteriri.


myList = [5, 10, 15, 5, 20, 15, 5, 10, 5, 100, 10, 20, 15, 100, 5, 10]


def iterativeFibonacci(n: int) -> int:
    x, y, = 0, 1

    for i in range(n):
        x, y = y, x + y
    return x


# Yukarıda bir myList listesi var ve bu liste içersindeki sayıların fibonacci degerlerini hesaplamak istiyoruz.
# Fakat liste icerisinde tekrar eden sayılar var, ve bu tekrar eden sayıların fibonacci degerleri de aynı olacaktır.
# işte memoization yani dinamik bir programlama mantıgında daha önce hesapladığımız ayni değerin sonucunu bir daha hesaplanmamalıdır ki
# makine daha kısa surelerde bosuna yorulmadan dinamik bir programımız olsun.

# yukarıdaki liste icin mesela 5 birden fazla kez tekrarlanıyor. Ozaman asagıdaki bir fonksiyon yazalım.
# Bir dictionary olusturalım ki daha önce hesaplanan aynı degerleri tutsun, burada 5 degerini dictionary e daha önce
# kaydedilip kaydedilmedigini kontrol etsin, kaydedilmemiş ise; yukarıdaki fonksiyondan hesaplasın ve kaydetsin.
# Eger ki hesaplamıs ise memory icindeki 5 değerinin sonucunu donsun.

memo = {}


def memoizationSolution(n):
    if n not in memo:
        memo[n] = iterativeFibonacci(n)
    return memo[n]


print(iterativeFibonacci(myList))
