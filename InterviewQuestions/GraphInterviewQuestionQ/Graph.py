# ReOrder Routes to make all paths lead to the city Zero

"""
There are "n" cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel
between two different cities(this network form a tree). Last year, The ministry of transport decided to orient the roads in one
direction because they are too narrow.

Roads are represented by "connectios" where "connections(i) = [a, b]" represents a road from city "ai" to city "bi".
This year, there will be a big event in the capital(city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city 0, Return this minimum number of edges changed.
it's guaranteed that each city can reach city 0 after reorder.

Example 1:

        3  <-2
     ->
     <-
    2
  ->
  <-
  0  <-4 -> 5
         <-

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Outout = 3
Explanation = Change the direction of edges show in red such that each node can reach the node 0 (capital).
"""

"""
SOLUTION:
    ilk önce boşta olan bir vertex yani boşta olan bir şehir olmadığını sorunun bana verdiği bilgilerden biliyorum.
    daha sonra bu graph in circle oluşturmayacağını biliyorum cunku n tane city varsa
    n-1 tane edge yani baglantı olacagı verilmis.
    
    Graph lar icinde DFS ve BFS algoritmaları kullanılabilir. Cunku Graph larda bir nevi agactır.
    Bu soru icin DFS ile cozulebilir.
    0 dan baslayarak, 0 'ın komşusuna bakarız ve eger ki edge 0 a gidecek sekilde degistirilmek gerekirse 0(cunlu tüm sehir ler 0 a girtmeli) 
    counter'i 1 arttırır. daha sonra 1 in komşusuna bakarım ve değiştirilmesi gereken durumlarda counter i arttırırım.
    aynı zaman da visitedCity diye kontorülünü yaptıgım vertex leri tekrar bos yere kontrol etmemek icin burada tutarım
    
    
    # GENEL bir bilgi
     listeler de index ile veri aramak O(1) iken, Value ile deger aramak O(n) dir.
     [0,1] in [[0,1],[1,3],[2,3],[4,0],[4,5]] yani bunun time comp. -> O(n) olur.
     
     oysa ki, bu deger aramasını bir hashset ile yapsaydık ozaman time complecity O(1) olurdu.
     (0,1) in {(0,1),(1,3),(2,3),(4,0),(4,5)}
     
"""

class Solution:
    def minOrder(self, n, connections) -> int:
        edges = set()

        for a,b in connections: # Listeyi set e cevirme
            edges.add((a,b))

        # Soruda bize matrix olarak verilmisti, biz bunu sözlüge cevirmek daha dogru olacaktır.
        neigbours = {}

        # Bos sözlükler yarattık
        for city in range(n):
            neigbours[city] = []
        # Bu bos sözlüklere matrix teki degerleri ekledik.
        for a,b in connections:
            neigbours[a].append(b)
            neigbours[b].append(a)

        counter = 0

        visited = set() # Dinamik proglama icin yapıldı

        def dfs(city):
            nonlocal edges, neigbours, visited, counter
            for neigbour in neigbours[city]:
                if neigbour in visited:
                    continue
                if (neigbour, city) not in edges:
                    counter += 1
                visited.add(neigbour)
                dfs(neigbour)

        visited.add(0)
        dfs(0)
        return counter




sol = Solution()


print(sol.minOrder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))