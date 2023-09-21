# Sequential Searching List
from typing import List


class SearchAlgorithms:
    def sequentialSearchUnordered(self, unOrderedList: List[int], number):
        ix = 0
        found = False

        while ix < len(unOrderedList) and not found:
            if unOrderedList[ix] == number:
                found = True
            else:
                ix += 1
        return found

    def sequentialSearchOrdered(self, orderedList, number):
        ix = 0
        found = False
        tooBig = False

        while ix < len(orderedList) and not found and not tooBig:
            if orderedList[ix] == number:
                found = True
            else:
                if orderedList[ix] > number:
                    tooBig = True
                else:
                    ix += 1
        return found

    def binarySearch(self, orderedList, number):
        firstPointer = 0
        lastPointer = len(orderedList) - 1

        found = False

        while firstPointer <= lastPointer and not found:
            midPoint = (lastPointer + firstPointer) // 2  # // integera çevirer. 2.5 --> 2 olarak verir.

            if orderedList[midPoint] == number:
                found = True
            else:
                if number < orderedList[midPoint]:
                    lastPointer = midPoint - 1
                else:
                    firstPointer = midPoint + 1
        return found


searchAlgoritm = SearchAlgorithms()

myList = [40, 20, 10, 4, 5, 19, 80, 2, 0, 14]
print(searchAlgoritm.sequentialSearchUnordered(myList, 2))
myList.sort()
print(searchAlgoritm.sequentialSearchOrdered(myList, 2))
print(searchAlgoritm.binarySearch(myList, 2))
