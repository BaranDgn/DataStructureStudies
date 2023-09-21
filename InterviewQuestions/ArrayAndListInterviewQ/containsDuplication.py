import array as arr

# Contatains Duplication - MICROSOFT INTERVIEW

myList = [1, 3, 2, 3, 4, 5, 6]

# Brute Froce
# time complexity = O(n^n)
# space complexity = O(1)
isDup = False
for i in range(0, len(myList)):
    for j in range(0, len(myList)):
        if (j == i):
            continue
        elif (myList[i] == myList[j]):
            isDup = True

print(isDup)


# Diğer bir yol ise; listeyi kücükten buyuge sıralayarak
# liste icerisindeki elemanların ilkine x, ikincisine y diyerek
# her bir elemanı gezerek listeyi kontor edebiliriz.(x ve y her seferinde bir sonraki indexli elemanı kontrol edecek.)
# time complexity --> O(NLogN)
# space complexity --> O(1)


# mülakatçı bana zamandan tasarruf et ve yer konusunda daha rahatsın dediğinde nasıl yapılır?
# time com. --> O(n)
# space com. --> O(n)
# bunu isteseydi;
# Hastset kullanılarak yapılabilir. Hashset icersinde her degerden uniqe bir deger olur.

# myList = [1, 3, 2, 3, 4, 5, 6]

def solution():
    hashSet = set()
    for num in myList:
        if num in hashSet:  # liste icerisindeki eleman hashset te var mı diye kontrolunu yapar.
            return True
        hashSet.add(num)
    return False


solution()


# en kolay cozum bu bakıldıgında.
# liste icersindeki eleman sayısı ile hashset icersindeki eleman sayısı birbirine esit degilse
# tekrarlanan eleman yoktur denebilir. Cunku hashset tekrarlana elemanlardan sadece birini alacaktır.
def solution2():
    return len(myList) != len(set(myList))


solution2()

# Müllkatçıın bekledigi.
# Bir sorunun cozumunu bulmak ve bu cozumlerden hangisini sececegimizi
# time ve space complexity ye gore degerlendirmek ve acıklaya bilmek bizden beklenendir.



