# BIG O NOTATION

# Time Complexity

# O(n)
def bigon(n):
    for i in range(0, n):
        print(i)


# O(n^2)
def bigon2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)


# O(n^3)
def bigon3(n):
    for i in range(0, n):
        for j in range(0, n):
            for z in range(0, n):
                print(i, j, z)

# O(log n)
import math


def logn(n):
    while n > 1:
        n = math.floor(n / 2)
        print(n)


# O(n log n) --> sorting algorith lerde oldukca yaygın kullanılır
def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n / 2)
        for i in range(1, lim):
            print(i)


# O(n!) --> algoritma n! kadar cagrılır.
def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0, n):  # 0 0 0 0 1 1 0
            print(i)
            nfactorial(n - 1)  # recursive


# nfactorial(4)
#  O(1) -- O(log n) -- O(n) -- O(n log n) -- O(n^2) -- O(2^n) -- O(n!)


# Space Complexity

# - buyuk o gosterimi sadece zaman icin degil yer icinde bir gosterim modelidir.

my_list = [10, 30, 40, 10, 5, 3, 2]
# yukaridaki dizi elemanlarini siralama yapildiginda, eger dizi icerisinde yer degistirme yapilirsa
# o halde O(1) notation da bu hic extra yer sorunu olusturmadan bu degistirme islemi yapılır.

# Eger bir baska dizi daha olusturup, onun icine sıralı elemanlari koymamız O(n) bir yer maliyeti cıkarar.
# n icin eleman sayisi denebilir.

# Mesela su gibi celiskiler olabilir. 2 dizi kullanarak sıralama yaparız ve yer maliyetinden feragat ederiz,
# fakat zaman complexity i O(n log n) yaparak zamandan tasarruf edebiliriz.
# bu gibi durumlarda zamandan mı yoksa yer den mi feragat edecegimiz yapılan projeye gore degisir.

my_list.sort()


def sort2(listem):
    for i in range(0, len(listem) - 1):
        if listem[i] > listem[i + 1]:
            listem[i] = listem[i + 1]
            listem[i + 1] = listem[i]
        else:
            continue
    return listem


print(sort2(my_list))

# Sorting Algoritms
