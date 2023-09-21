# DAILY TEMP - FACEBOOK/META


"""
Given an array of integers tempratures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the i^th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i]
== 0 instead.

Example 1:
Input: temperatures = [73, 74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
myInput = [73, 74, 75, 71, 69, 72, 76, 73]

""" 
    bir dizi olustururuz.(dizi cunku boyutu onceden belli bir case var, aynı zamanda boyutunu da asmamıs oluruz.). Output'u tutması icin
    daha sonra inputtan her gelen sayıyı stack e ekler ve bir öndeki sayıs ile karsılatırırız.
    Eger son eklenen sayı bir öndekineden buyukse, aralarındaki index farkını alıp, diziye ekleriz.
    Eger ki buyuk degilse ozaman;
        eklemeye devam ederiz. ve yeni eklediğimizi bir onceki ile karsılastırırız, index farkını diziye ekleriz
        aynı zamanda o anda output dizisine bir sey eklemediğimiz sayıyı da ondan daha buyuk bir sayı geldiginde index farkını ekleriz.
        
        Her bir sayının index farkı degerini yine her sayının output dizisindeki indeksine karsılık gelecek sekilde ekleriz.
        
        Önemli noktalardan biri ise; makineye bos yere is yaptırmamak için dizinin tum elemanlarını 
        basta 0 yapabiliriz ki, kontrol ettigimiz sayıdan daha buyuk sayı olmadıgında varoalan hali ile kalabilsin. 
         
buna monoton azalan stack denir.

enumerate sayesinde bu sekilde yazabildik.
[[73, 0], [74, 1], [75, 2], [71, 3], [69, 4], [72, 5], [76, 6], [73, 7]]
"""

temp = [73, 74, 75, 71, 69, 72, 76, 73]


def solutionUdemy():
    result = [0] * len(temp)
    myStack = []  # hem temp leri hemde index leri koyacagız [temp & index]

    for ind, temperature in enumerate(temp):
        while myStack and temperature > myStack[-1][0]:  # myStack!= null
            stackTemp, stackIndex = myStack.pop()  # pop burada onde yapıldı ki son eklenen, eklenmeden once bir onceki deger silinsin. Sonra yeni deger eklensin
            result[stackIndex] = ind - stackIndex

        myStack.append([temperature, ind])
    return result

"""
    [73, 74, 75, 71, 69, 72, 76, 73]
    yukarıdaki input bize verilen temperatures degerleridir.
    
    ilk basta bir result tanımladık: bu result bizden istenen output u koyacagımız dizi. 
    Ilk basta 0 atadık ki daha buyuk deger olmadıgında 0 kalsın ve biz 0 eklemek ile ugrasmayalim(soruda daha buyuk deger olmadıgında 0 degeri alır diyor. Ayrıca verilen inputtaki son deger de 0 alır cunku kıyaslayacagı bir sonraki deger yok)
     daha sonra myStack isimli bir stack(aslında liste burada liste kullandık ama mantık olarak stack, python da liste ile stack arasında cok fark yoktur.)
     bu myStack hem temperature hem de bunların indexlerini [[temp, indexi],[temp, indexi],[temp, indexi]..] sekilde yaptık.
     
     daha sonra for icinde enumerate kullandık: bu sayede [temp, index] olarak myStack icersinde degerleri atabildik.
     
     while da ilk basta mystack var mı diye kontrol ettik yoksa ilk degeri
     append edecek yani [73, 0] diye.
     var ise temperature dan aldıgı 74 degerini myStack teki [73, 0] --< 73 degeri ile kıyasladı
     eger buyuk ise 74 stack e eklemeden 73 ü mystackten cıkardı ve cıkarırkende degeri ve indegi 2 farklı degiskende tuttu.
     bu sayede 73 un indexi ile 74 un indeksini birbirinde cıkrarak farkı buldu ve resultun cıkarılan 73 olan indeksine attı.
     daha sonra [74,1] olarak myStack icersinde ekledi.
     
     bu algoritmaya göre devam etti, kıyaslanana deger while i saglamadıgında bu degeri sadece myStack e ekledi ve saglaya deger gel
"""

print(solutionUdemy())




# Need to improve
def solution():
    output = []
    day = 0
    for i in range(0, len(myInput) - 1):
        for j in range(1, len(myInput) - 1):
            if myInput[i] > myInput[j]:
                day += 1
                break
            else:
                day += 1
        output.append(day)
        day = 0
    return output


print(solution())
