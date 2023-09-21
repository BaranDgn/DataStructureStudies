# MAJORITY ELEMENT - FACEBOOK- META

"""
Given an array of size n, return the majority element

The majority is the element that appears more that (n/2) times.
You may assume that the majority element always exists in the array.

Example1 :
Input : nums =[3,2,3]
Output : 3

Example2 :
Input : nums= [2,2,1,1,1,2,2]
Output : 2

constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -10^3<= nums[i] <= 10^9
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
# Ways of solution methods, We used so far:
# brute - force
# sorting
# binary manipulation

"""
# For this problem above;
[2,2,1,1,1,2,2]


1- solution -- Easy-Thinking way
bunları bir sozluge yada hashmap e atarım ve soyle olur:
{1 : 4, 2 : 1} gibi. ve daha sonra adetlerini takip ederim, en buyugunu bulup yazdırırım.


1- SOLUTION -- BOYER MOORE ALGORITHM- Majority Algorithm - 
Her zaman majority varsa kullanılabilir.
Linear zamanda O(n), O(1) space de yapıldı.


"""
input1 = [2, 2, 1, 1, 1, 2, 2]
input2 = [3, 2, 3]
input3 = [10, 10, 5, 6, 5, 5, 5, 4, 5]


# SOLUTION 1
# Time Complexity -- O(n)
# Space Complexity -- O(n)
def findMajority(input):
    numbers = {}
    result = 0
    maxNumber = 0
    for i in input:
        numbers[i] = 1 + numbers.get(i, 0)
        if numbers[i] > maxNumber:
            result = i
        maxNumber = max(maxNumber, numbers[i])
    return result


# SOLUTION 2
def boyerMoore(input):
    result = 0
    count = 0
    for num in input:
        if count == 0:
            result = num
        # if num == result:
        #    count += 1
        # else:
        #    count -=1
        count += 1 if num == result else -1
    return result


print(boyerMoore(input3))
