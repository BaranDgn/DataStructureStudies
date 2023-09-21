# FIBONACCI

# Altın oran ı olusturur.
# bir önceki sayıların toplanarak kendisini oluşturan sayıdır.
# 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 ...


# REcurive de mutlaka ve mutlaka bir çıkış durumu yazılmalıdır.
# Aksi halde sonsuz döngüye girecektir.
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), for n>1.

Given n, calculate F(n)

Example 1:
Input: n = 2
Output = 1
Explanation : F(2) = F(1) + F(0) = 1+0=1.

Example 2:
Input: n = 3
Output = 2
Explanation : F(3) = F(2) + F(1) = 1+1=2.

Example 3:
Input: n = 4
Output = 3
Explanation : F(4) = F(3) + F(2) = 1+2=3.
"""


def recursiveFibonacci(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
    # f(3) + (2)
    # f(2) + f(1) + f(2) + f(1)


print(recursiveFibonacci(9))


# Solution with iterative

def iterativeFibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y

    return x


print(iterativeFibonacci(6))
