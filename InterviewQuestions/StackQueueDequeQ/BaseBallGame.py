# BASEBALL - MICROSOFT

"""
You're keeping a score for a baseball game with starange rules.
The game consists of several rounds, where the scores of past rounds may affect
future round scores.

At the beginning of the game, you start with an empty record. you are given a list strings ops,
where ops[i] is the i^th operation you musy apply to the record and is one of the following:
1. An integer x -Record a new score of x.
2. '+' - record a new score that is the sum of the previous two scores. It is guareanteed there will always be a previous score.
3. 'D' -record a new score that is double the previous score. it is guaranteed there will always be a previous score.
4. 'C' - Invalidate the previous scıre, removing it from the record. It is guareanteed there will always be a previous score.

Return a sum of the all the scores on the record. The test case are generated so that the answer fits in a a 32-bir integer.

EXAMPLE1:
Input: ops= ["5", "2","C","D","+"]
Output = 30
Explanation:
"5" -Add 5 to record, record is now[5]
"2" -Add 2 to record, record is now[5,2]
"C" -Invalidate and remove the previous score, record score is now [5].
"D" -Add 2*5 = 10 to record, record is now[5,10].
"+" -Add 5 + 10 = 15   to record, record is now[5,10, 15]
the total sum is 5 + 10 + 15 = 30

"""

myInput = ["5","2","C","D","+"]
def solution():

    myStack = []

    for op in myInput:
        if op == "C":
            myStack.pop()
        elif op == "+":
            myStack.append(myStack[-1] + myStack[-2])
        elif op == "D":
            myStack.append(2 * myStack[-1])
        else:
            myStack.append(int(op))
    return sum(myStack)

print(solution())



