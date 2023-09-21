# REVERSE STRING

"""
Write a function that reverse a string. The input string is given as an array ıf character s.
You must do this by modifying the inout array in-place with O(1) extra memory.

Example 1:
Input: s = ["h", "e", "l","l","o"]
Output:  ["o", "l", "l","e","h"]

Constraints:
1<=s.length <=10^5
s[i] is a printable ascii character
"""

myInput = ["h", "e", "l", "l", "o"]
myArray = ["h", "e", "l", "l", "o"]

# Solution 1
myInput[0], myInput[-1] = myInput[-1], myInput[0]
print(myInput)
myInputTwo = ["c", "o", "f", "f", "e", "e"]


def reverseRecursive(s, start: int, end: int):
    if start > end:
        return
    s[start], s[end] = s[end], s[start]
    reverseRecursive(s, start + 1, end - 1)


print(reverseRecursive(myInput, 0, len(myInput) - 1))
