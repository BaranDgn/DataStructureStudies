# Remove Node from the end of linked list


"""
Given the "head" a linked list, remove "n^th" node from the end of the list and return its head

Example 1:

1   2   3   4   5

1   2   3   5

Input : head =[1,2,3,4,5], n=2
Output = [1,2,3,5]

Input : head = [3], n=1
Output : []

Input : head = [1,2], n=1
Output : [1]
"""
from typing import Optional

"""
Linked list sorularında ikili pointer ile sorunun cozumu olabilir m idiye dusunulmelidir

Bu sorunun çözümü:
    
    
    1. Başlangıçta x ve y i başlangıç node neresi ise oraya koyarız.
    1   2   3   4   5
    x,y
    2. Daha sonra x ve y nin arasına n değeri kadar bosluk bırakırız.
    n = 2
    1   2   3   4   5
    x       y
    
    3. daha sonra x ve y yi adım adım sağa ilerletiriz. Sonra y nin bir sonraki node u Null mı diye kontrol ederim 
    boş değilse devam ederim.
    1   2   3   4   5
        x       y
    4. y nin bir sonraki node ı Boş olmadığı için tekrar sağa kaydırdım.
     1   2   3   4   5
             x       y 
    y nin next node boş oldugunda; sona geldigimi anlarım.
    Sona geldiysem ve arada da n kadar bosluk bıraktıysam.
    x cıkartılacak olan node bir öncesinde olacaktır. 
    bu x in üzerinde olduğu node un pointerini son node olarak verirsem
    4 yani n=2 ile istenen deger cıkartılmış olur.
    bunu da yapabilmek için x.next(3 ün pointerı) = x.next.next(5 e esitlenir) e esitlenir böylece 4 silinir.
    
    Böylece; time Comp : O(n), space Comp : O(1) olur


Bu yönteme window sliding denir.
    
"""


# CREATING A LINKED LIST
class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next_node
        print("None")


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.display()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1   2   3   4   5
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        leftPointer = head
        rightPointer = head

        # n >0 ve rightPointer null olmadığı surece, bos bir liste veya n=3 oldugu durumlar icin kontrol edilmeli
        # Bu blokta x ve y degiskenleri arasında n kadar bosluk bıraktık.
        # Böylece y 3 ü gösteriyor.
        while n > 0 and rightPointer:
            rightPointer = rightPointer.next
            n -= 1

        # rightPointer ve rghtpointer in bir sonraki node i null olmadıgı surece.
        # Bu blokta ise x ve y degerlerini birer birer sağa kaydırıyoruz,
        # taki y nin next node null olana kadar
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        # Linked liste de eleman olmamasına karşı veya tek bir eleman varsa
        # leftpointerin null-check kontrolu yapılmalıdır.
        # Burada bir önemli nokta, yukarıdaki kodları calıstırdıktan sonra x head e ve y de null ise
        # tek bir elemandır gibi diyebiliriz.
        if leftPointer == head and not rightPointer:
            return head.next #  bos bir liste dondurur

        # y nin next node ı null ise leftpointer in gösterdiği node yani
        # silinmesini istediğimiz node ı gösteren(bir önceki node)
        # pointer ini 5 e eşitledik. Böylece 4 silindi.
        leftPointer.next = leftPointer.next.next

        return head
