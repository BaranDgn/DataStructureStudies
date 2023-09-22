# Data Stream - Microsoft

""" Hard***
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and median is the mean of the two middle values.

    for example, for arr= [2,3,4], the median is 3.
    for example, for arr= [2,3], the median is (2+3)/2 = 2.5.

implement the MedianFinder class:
    MedianFinder() initializes the MEdianFinder object.
    void addNum(int num) adds the integer num the data stream to the structure.
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input:
["MedianFinder", "addNumber", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null,null,null,1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder()
medianFinder.addNum(1); // arr=[1]
medianFinder.addNum(2); // arr=[1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1+2)/2)
medianFinder.addNum(3); // arr=[1, 2, 3]
medianFinder.findMedian(); //return 2.0
"""

"""
SOLUTION:
    2 adet heap olusturaalım. Biri girilen elemanların kücüklerini tutsun,
    diğeri ise büyüklerini tutsun. 
    
    kücükleri tutan heap i maxi heap yaparsak, O(1) zamanda en üstteki değer, en büyük değeri verecektir.
    
    büyük leri tutan heap ise min heap yapılırsa, yine O(1) zamanda en üstteki yani en küçük değeri verecektir.
    
    Bu şekilde median i bulabilmek için ortancaları bulmuş oluruz.
    
    Aynı zamanda 2 heap in eleman sayıları birbirinden en fazla 1 fazla olabilsin aksi taktirde median yanlış olabilir.
    çünkü;
    
    heap 1 : 1 2 3 4 en büyüğünü alırız --> 4 
    heap 2 : 6 7 --> en küçüğünü alırız --> 6
    
    Bu 2 sinin ortalaması bize yanlış mediani verir. Doğru median için 3 4 in ortalamasını almak gerekir. Çünkü en oratadaki 2 sayı onlardır.
    Bu durumda heap1 den heap 2 ye heap1 deki en büyük sayı gider.
    heap1 : 1 2 3 --> 3
    heap2 : 4 6 7 --> 4
    
    Ayrıca her eleman ekleme işlemi dinamik olarak yapıldığı için heap1 e heap2 de bulunan degerlerden daha büyük bir
    değer gelme olasılığını da kontrol etmeli, gelmesi taktirde bunu heap 2 ye göndermeliyiz.


    Ekleme işlemi bittikten sonra median işlemi çok daha kolay, 2 heap in boyutlarına göre
    if ler ile istenen deger return ettirilir.
"""
# O(N²) — Quadratic Time

import heapq


class MedianFinder:
    def __init__(self):
        self.smallHeap = [] # kücük değerli verileri tutacak, en büyük elemanı bulabilmek icin max heap kullanacak fakat pythonda max heap yok, bu nedenle -1 ile çarpılacak elemanlar.
        self.largeHeap = [] # büyük değerli verileri tutacak, en kücük elemanı bulabilmek için min heap kullanacak

    def addNum(self, num: [int]) -> None:
        heapq.heappush(self.smallHeap, num * -1)

        # Eger small heap e, large heap ten daha büyük bir değer gelmiş ise, yer değiştirmeleri için
        # Ayrıca smallheapi -1 ile çarpmamaızın sebebi python da max heap olmadığı için, burada ki en buyuk deri max heap gibi kullanarak almayı saglar.

        if self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0] > self.largeHeap[0]):
            value = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, value)

        # Her iki heap teki elemanların sayısı eşit yada en fazla 1 fazla olmalı, bunu kontrol ediyoruz
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            value = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, value)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            value = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * value)
    def findMedium(self):
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        return (-1 * self.smallHeap[0] + self.largeHeap[0]) / 2

medianFinder = MedianFinder()
medianFinder.addNum(3)
print(medianFinder.addNum(5))
print(medianFinder.findMedium())
medianFinder.addNum(9)
print(medianFinder.addNum(7))
print(medianFinder.findMedium())