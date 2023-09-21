# Duplication Linked List

"""
Given an array of integers nums containing n+1 integers where each integer is in the range(1,n) inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and users only constant extra space.

Example 1:
Input : nums = [1,3,4,2,2]
Output : 2

Example 2:
Input : nums = [3,1,3,4,2]
Output : 3

constraints:
    1 <= n < = 10^1
    nums.length == n+1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow-up:
How can we prove that at least one duplication number must exist in?
Can you solve the problem in linear runtime complexity?
"""

"""
Solution1:
    verilen listeyi sort ederek, buyukten kucuge sıralarız.
    Daha sonra tekrarlayan rakamlar yan yana geleceğinde kontrol edip buluruz.
    Fakat soruda Listeyi modify etme diyor.
    time comp-> O(nlogn) de bulunur
    space comp-> O(1) de bulunur.
    
Solution2: 
    extradan hashset veya hashmap olusturup, hashset--> tekrarlana verileri almaz. 
    2 listenin uzunluklarının kıyaslarız farklı cıkarsa tekrarlana ver var deriz.
    Fakat Extra space de kullanamazsın diyor.
    
Solution3: 
    Bir diğer yöntem ise 2 for loop a sokarak sırasıyla bütün listeyi gezeriz
    time comp-> O(n^2) de bulunur
    space comp-> O(1) de bulunur.
    Fakat bu yöntemde verimsiz olur. Ayrıca Linear time demiş yani O(n de istiyor)
    
Solution4: FLOYD CYCLE DETECTION ALGORITH
    Buradaki listeyi bir linked liste cevirip, linked list içersinde de
    cycle detection denilen bir döngü olusturup çözülebilir.
    
    FLOYD CYCLE DETECTION ALGORITH: Linked list lerle calısırken bir döngu oluştuğunda, tekrar eden elemanları bulmak için
    Floyd tarafından geliştirilmiş bir algoritmadır.
    
    How is Floyd working?
    
    Floyd un buldugu algoritmaya gore;
    Floyd 3 değişken olusturmamız istiyor ve bu değişkenler node lar uzerinde ilerlesin.
    Bu degiskenlerden 2 si yavaş ilerlesin ve 1 de hızlı ilerlesin diyor.
    Floyd ilk indexteki node'un tekrarlanan node'a olan uzaklıgının
    ilk başta yavaş değişken ile 2. hızlı değişkenin ilk kesiştiği node'un tekrar lanan rakamın bulunduğu
    node'a olan uzaklığı bir birine eşittir diyor. (Matematiksel olarak  buluyor.)
    
    Teoremin şemalı gosterimi:
    
    [1,3,4,2,2]
    y: fast
    x: slow 
    1 -> 3 -> 4
         ↑    ↓
         |----2
    
    1. Adım     
         x    y   x 1 adım giderken, y 2 adım gidiyor(bunlar kesin bu şekilde değil birinin diğerinde hızlı gittigini göstermek için kullanıldı.)
    1 -> 3 -> 4
         ↑    ↓
         |----2
    
    2.Adım
         y    x   
    1 -> 3 -> 4
         ↑    ↓
         |----2
         
    3.Adım
               
    1 -> 3 -> 4
         ↑    ↓
         |----2
              x y  3. adım da x ve y ilk kez bir node uzerinde kesiyorlar.
              simdi floyd un dediği gibi 3. slow değişkeni ekleyelim.
              ve 2 slow değişken olan x ve z nin nerede kesiştiğine bakalım.
              x kaldığı node dan decam ederken, z ilk node dan baslar.
    
    4.Adım
    z           
    1 -> 3 -> 4
         ↑    ↓
         |----2
              x ,y
    
    5.Adım
        z x            z ve x ilk adımlarında 3 te kesiştiler, bu algoritmaya göre 
    1 -> 3 -> 4        Floyd 3 değerinin yani bu node ta bulunan değerin duplication value
         ↑    ↓         tekrarlanan değer olduğunu söyler.
         |----2
              y
    
Başka bir Veri seti ile:
    x:slow
    y:Fast
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4    
    
    1. Adım
        x       y
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4    
    
    2. Adım
            x   
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4 
                y
                
    3. Adım
            y   x
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4 
    
    4. Adım
               
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4 
                x , y // x ve y 4. adımda 4. node a kesişti. Şimdi diğer slow z değişkeni ilk node dan başlayacak         
    5. Adım
    z        
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4 
                x , y
    6. Adım
        z        
    0 → 1 → 2 → 3
            ↑   ↓  
            5 ← 4 
            x    y
    7. Adım
           z,x        // z ve x değişkeni 3. node da ve value sunun da 2 kabul edersek
    0 → 1 → 2 → 3     // 2 nin tekrarlanan deger oldugunu soyleyebiliriz.
            ↑   ↓      // aynı zamanda semadan da bakıdığına hem 5 hemde 1
            5 ← 4      // 2 ye gidiyor. Buradan da 2 nin tekrarlanan bir değer olduğunu söyleyebilir. 
                y
"""
myInput = [1, 3, 4, 2, 2]


def floyd():
    slowPointer = 0
    fastPointer = 0

    while True:
        slowPointer = myInput[slowPointer]
        fastPointer = myInput[myInput[fastPointer]]
        print("First Pointer InterSection")
        print(slowPointer, " ", fastPointer)
        if slowPointer == fastPointer:
            break

    secondSlowPointer = 0
    while True:
        slowPointer = myInput[slowPointer]
        secondSlowPointer = myInput[secondSlowPointer]
        print("Second Pointer InterSection")
        print(slowPointer, " ", secondSlowPointer)
        if slowPointer == secondSlowPointer:
            return slowPointer


print(floyd())


# Duplication in List O(n^2) zamanda ama soruda O(n) linear zamand istiyor.
def solution():
    for i in range(0, len(myInput)):
        for j in range(i + 1, len(myInput)):
            # print(myInput[i], " ", myInput[j])
            if myInput[i] == myInput[j]:
                return myInput[i]

# print(solution())
