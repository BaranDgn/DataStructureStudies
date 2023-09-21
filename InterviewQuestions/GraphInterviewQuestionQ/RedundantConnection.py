# Redundant Connection

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with 'n' nodes labeles from '1' to 'n' with one additional edge added.
The added edge has two different vertices chosen from '1' to 'n', and was not an edge that already existed. The graph is represented
as an array 'edges' of lenght 'n' where edges[i] = [ni, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of 'n' nodes. If there are multiple answers,
return the answer that occurs last in the input.

Example 1:

1 -- 2
|   |
 3

Input : edges = [[1,2],[1,3],[2,3]]
Output: [2, 3]


Input : edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1, 4]

5
|
1 -- 2 -- 3
|         |
4 --------

"""
from _ast import List

"""
NEW ALGORITH - UNION-FIND ALGORITHM

used it to detect cycle in a graph. 
Graphlarda kullanılabilecek bir algoritmadır.
Baglama islemlerini verimli ve parentları neye baglandıgını takip ederek yapabilmeyi sağlar.

Union-find a göre;
2 önemli nokta vardır. Birincisi Parents, ikincisi ranks dir.
union-find algorith parent node ları bir liste icinde tutup bunların ranklarini de baska bir listede tutar.

Path Compression:
butun node ları root a baglarız. 

örnegin;
4 node lu bir graph var, birde 3 node lu bir graph var. Bu 2 node u birbiri ile birlestirmek istesen der union
rank i buyuk(yada size, burada 4 node lu graph ın rank daha buyuktur.) olan parent olur der.
kucuk olan da child olur.

Yukarıdaki soru icin nasıl uygulanır?
simdi ilk input icin denersek;
1 2 ve 3 node larımız var, ve bunları basta baglı olmadıkları, her birinin kendi basına bir node olduğunu yada agac oldugunu kabul edelim.
Böylece her bir agacın parent i kendisi olur.
bir parent listesi olustururuz. parent = [1,2,3]
bir de rank lerinin listesini olusturalım = [1,1,1] // burada hic birinin bir child i olmadıgı icin tek bir node dan olustukları icin 1 oldu. 

şimdi bize verilen edges larla bir kontrol yapalım.
[1, 2] yani 2 node 1 e baglıyor. ozaman parent ta 2 yerine 1 yazalım cunku 2 nin parent i 1 oldu ve 1 in size/rank ini 2 yapalım.
parent = [1,1,3] rank=[2,1,1]

daha sonra [1,3] bir birine baglı imis, ozaman 3, 1 e baglı oldugu icin; 3 ün de parent i 1 oluyor.
parent = [1,1,1] rank = [3,1,1] oldu.

simdi bakıldıgında 2 node aynı parent node a baglı ise olusturacakları yeni baglantı bir circle olusturacagından 
bunu buluruz.

"""

from typing import List


class Solution:

    def findReduntantConnnection(self, edges: List[List[int]]) -> List[int]:
        parents = []  # 1 2 3

        for i in range(len(edges) + 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)

        def find(n):
            p1 = parents[n]
            while p1 != parents[p1]:
                # Path compression
                parents[p1] = parents[parents[p1]]
                p1 = parents[p1]
            return p1

        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            if parent1 == parent2:
                # connected
                return False
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True

        for n1, n2 in edges:
            # print(n1, " ", n2)
            # print("--")
            if not union(n1, n2):
                # print(n1, " ", n2)
                return [n1, n2]


sol = Solution()
print(sol.findReduntantConnnection([[1, 2], [1, 3], [2, 3]]))
print(sol.findReduntantConnnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
