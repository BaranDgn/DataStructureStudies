# Intersection Of Two Linked Lists

"""
Given the heads of two linked-list "headA" and "headB", return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null

For example the following two linked lists begin to intersect at node c1

A:      a1 ->   a2 -|
                    c1 -> c2-> c3
B:  b1 -> b2 -> b3-|

the test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note: that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows(your program is not given these inputs)

    intersection - the value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list
    listB    Te second linked list
    skipA - The number of nodes to skip ahead listA(starting from the head) to get to the intersected node.
    skipA - The number of nodes to skip ahead listB(starting from the head) to get to the intersected node.

    The Judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
    if you correctly return the intersected node, then your solution will be accepted.

"""
"""
Solution of the case:
    x ve y pointer ları olusturduk. Ilk başta x, a lar için, y ise b ler den başladı.
    şimdi A ve B nin kesiştiği yer C1, fakat x ve y point larını aynı anda hareket ettirdiğimizde
    a ların node sayısı b lerin node sayısında az oldugu icin 
    2 pointer aynı anda C1 i gösteremiyor.
    
    Bunu çözebilmek için bir döngü içerisinde x ve y pointer larını null kadar götürüp nul dan sonra 
    x in head ni b ye y nin head ni a node larından başalayacak şekilde tekrar gezdiğimiz C1 de kesişirler
    Buradaki öndemli nokta pointer lar 2. sefer node larda dolaşacağı zaman ilk başladıkları head kısımlarının yerini değiştirmektir.
    (Çarpmadaki çarpım kuralı gibi. 2 çarpanın yeri değişsede aynı sonucu verir)
     
     1. adım
          x
          a1 -> a2 -|
                    c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|
    y    
    2. adım
                x
          a1 -> a2 -|
                    c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|
          y
    3. adım
                
          a1 -> a2 -|  x
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|
                y
    4. adım
                
          a1 -> a2 -|       x
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|  y
    
    5. adım
                
          a1 -> a2 -|             x
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|        y       

    6. adım
                                        (buradan sonra x; b node'a gider)
          a1 -> a2 -|                   x
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|        y  
    
    7. adım
                                        
          a1 -> a2 -|                   
                      c1 -> c2 ->c3 -> Null
     b1 -> b2 -> b3 -|               y  (buradan sonra y; a node'a gider)
      x
    
    8. adım
           y                             
          a1 -> a2 -|                   
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|               
           x
    9. adım
                y                             
          a1 -> a2 -|                   
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -|               
                x
    
    10. adım : Görüldüğü gibi x ve y aynı anda 2 linked list in kesiştiği intersection da bulundu.
                                             
          a1 -> a2 -| y                 
                      c1 -> c2 ->c3 -> Null
    b1 -> b2 -> b3 -| x       
    
    time comp : O(n) yada O(n +m) de olabilir, space Comp O(1)                   
"""


def solution(headA, headB):
    firstPointer = headA
    secondPointer = headB

    while firstPointer != secondPointer:
        # burada hem next ile adım adım gitmesini kontrol ettim.
        # hemde null-check yaparak, linked list sonuna gitmiş ise tam tersi node dan baslamasını sagladım pointer in.
        firstPointer = firstPointer.next if firstPointer is not None else headB
        secondPointer = secondPointer.next if secondPointer is not None else headA
    return firstPointer  # SecondPointer da dondurulebilir. Ikı aynı zaten
