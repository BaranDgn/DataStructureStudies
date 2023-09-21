# SINGLE NUMBER - AMAZON INTERVIEW
"""
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity, and use only constrant extra space.

Example 1:
Input : nums = [2,2,1]
Output: 1

Example2 : nums = [4,1,2,1,2]
Outout : 4

Example3 : nums = [1]
Outout : 1

-----------
# Tek elemanlı olarak verdigi durumlara (example 3 )deki gibi EDGE-CASE denir.

"# You must implement a solution with a linear runtime complexity, and use only constrant extra space."
Burada verdiği şarta göre;
    linear runtime complexity --> O(N)
    Only constraint extra space --> O(1)
"""
input1 = [4, 1, 2, 1, 2]
input2 = [2, 2, 1]
input3 = [1]
input4 = [3,5,7,4,3,7,5]


# Bu srounun cozumu icin XOR kapısı mantıgını kullanabiliriz.
# XOR kapısında; sadece iki girdi birbirinden farklı oldugu durumlarda 1 olur.
# 0 0 --> 0
# 0 1 --> 1
# 1 0 --> 1
# 1 1 --> 0

# Bit Manipulation denir. Bit ler ile bir sorunun cozumunu bulmaya.
def solutionOfSingle1(input):
    result = 0 # xor with zero. zero does not change xor result.
    for num in input:
        result = num ^ result
        print(result)
    return result


print(solutionOfSingle1(input4))

"""
baslangıcta result degiskenine 0 atarız.
soyle bir dizide [4,1,3,1,3] sırasıyla;

4 XOR 0 = 4 -- 100 xor 000 -- 100
1 XOR 4 = 1 -- 001 xor 100 -- 101
3 XOR 5 = 0 -- 011 xor 101 -- 110
1 XOR 6 = 1 -- 001 xor 110 -- 111
3 XOR 7 = 0 -- 011 xor 111 -- 100
eninde sonunda her rakam bu degisken ile XOR islemine tuttulursa, bunların aynı olanları birbrini eler.

input4 = [3,5,7,4,3,7,5]

3 XOR 0 = 3 -- 011 XOR 000 = 011
5 XOR 3 = 101 XOR 011 -- 110
7 XOR 6 = 111 XOR 110 -- 001
4 xor 1 = 100 xor 001 -- 101
3 xor 5 = 011 xor 101 -- 110
7 xor 6 = 111 xor 110 -- 001
5 xor 1 = 111 xor 001 -- 110 
"""


"""
SUMMARY OF USING WAYS OF SOLUTION

Contains Duplication: 
1. Brute Force --> we check the list with two variable and use two for loops to do it. t.c.= O(n^n), s.c =O(1) 
2. We sorted all the elements in list and check the list by two for loops. t.c.= O(n^n), s.c = O(n) 
3. We used hashset that holds only unique values in it, and check if the duplicated value added in hashset before, if it does, return True.
4. We can also check the lenght of hashset and given list, if their lenght is not same, there is duplicated value in the list.

Majority Element:
1. bunları bir sozluge yada hashmap e atarım ve soyle olur:
{1 : 4, 2 : 1} gibi. ve daha sonra adetlerini takip ederim, en buyugunu bulup yazdırırım.

2. BOYER MOORE ALGORITHM- Majority Algorithm - Her zaman majority varsa kullanılabilir. Linear zamanda O(n), O(1) space de yapıldı.

Single Number:
1. Bit Manipulation - with XOR Logic Door.

"""