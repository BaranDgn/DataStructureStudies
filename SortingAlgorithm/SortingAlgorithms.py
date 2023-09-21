# Sorting Algorithms

class SortingAlgorithms:

    # Bubble Sort
    def bubbleSort(self, arr: [int]):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # print(i, " - ", j)
        return arr

    # Selection Sort
    def selectionSort(self, arr: [int]):
        for i in range(0, len(arr) - 1):
            minIndex = i
            for j in range(i + 1,
                           len(arr)):  # En sola yerlşetirilmiş elemanları tekrar tekrar gezmemek için i+1 olarak yaptık
                if arr[j] < arr[minIndex]:
                    minIndex = j
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    # Insertion Sort
    def insertionSort(self, arr: [int]):
        for i in range(1, len(arr)):
            temp = arr[i]  # kıyaslama yapılacak olan degeri tutugumuz degisken.
            j = i - 1  # i - 1 sayesinde hep kıyaslama yapılan degerin solundakileri kontrol ediyoruz.
            while temp < arr[
                j] and j > -1:  # j > -1 iki nedenle yapıldı,  birincisi j, -1 olup dizinin son indeksini göstermesin diye.
                arr[j + 1] = arr[j]
                arr[j] = temp
                j -= 1
        return arr

    # Merge Sort
    def merge(self, arr1: [int], arr2: [int]):
        firstPointer = 0
        secondPointer = 0
        mergedList = []

        while firstPointer < len(arr1) and secondPointer < len(arr2):   # Bölünmüs array lerin boyutlarını gecmemesi icin kontrol ederiz.
            if arr1[firstPointer] < arr2[secondPointer]:
                mergedList.append(arr1[firstPointer])
                firstPointer += 1
            else:
                mergedList.append(arr2[secondPointer])
                secondPointer += 1
        # 2 grubun Merge işlemi yapılırken en kucuk değer en basta olmak üzere yapılır
        # ve 2 diziden birinde en büyük değer yerleştirilmeyebilir.
        # çünkü 2 grubun en son indekslerindeki elemanlardan kücük olanı mergeList e yerleştirilince, her 2 dizinin pointer larından biri yukarıdaki koşulu saglamadıgı için
        # son eleman yerleştirilmeden işlem biter. Bu nedenle asagıda son elemanı yerleştirmek için yapılır.
        while firstPointer < len(arr1):
            mergedList.append(arr1[firstPointer])
            firstPointer += 1
        while secondPointer < len(arr2):
            mergedList.append(arr2[secondPointer])
            secondPointer += 1
        return mergedList

    def mergeSort(self, arr: [int]):
        # Exit condition
        # Bu recursive elemanlar birer tane kalana kadar calısır. Daha sonra merge icerisine sokar.
        if len(arr) == 1:  # Tek eleman varsa sıralı dizi denebilir.
            return arr
        midPoint = int(len(arr) // 2)
        leftPart = arr[:midPoint]  # bir dizinin orta noktasından soldaki değerleri almak icin.
        rightPart = arr[midPoint:]  # bir dizinin orta noktasından sağındaki değerleri almak icin.
        return self.merge(self.mergeSort(leftPart), self.mergeSort(rightPart))

    # Quick Sort
    def pivot(self, arr: [int], pivotIndex, endIndex):
        swapIndex = pivotIndex
        for i in range(pivotIndex + 1, endIndex + 1): # dizinin tüm elemanlarına ulaşabilmek için endpoint +1 yapıldı.
            if arr[i] < arr[pivotIndex]:
                swapIndex += 1
                arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
        arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
        return swapIndex

    def quickSort(self, arr: [int], leftPointer= 0, rightPointer= None):
        if rightPointer == None:
            rightPointer = len(arr) -1
        if leftPointer < rightPointer:
            swapIndex = self.pivot(arr, leftPointer, rightPointer)
            self.quickSort(arr, leftPointer,swapIndex -1)
            self.quickSort(arr, swapIndex+1, rightPointer)
        return arr

    #Heapify
    def heapify(self, arr: [int], n, i):
        largest = i
        leftInd = 2 * i + 1
        rightInd = 2 * i + 2
        # n --> dizi içindeki eleman sayısı
        if leftInd < n and arr[largest] < arr[leftInd]:
            largest = leftInd

        if rightInd < n and arr[largest] < arr[rightInd]:
            largest = rightInd

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Heap Sort
    def heapSort(self, arr: [int]):
        n = len(arr)

        # MAX-HEAP
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # Swap
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr





myArr = [10, 3, 4, 45, 65, 34, 54, 0, 1]
sorting = SortingAlgorithms()
print(sorting.bubbleSort(myArr))
print(sorting.selectionSort(myArr))
print(sorting.insertionSort(myArr))
print(sorting.mergeSort(myArr))
print(sorting.quickSort(myArr))
print("heap Sort: ", sorting.heapSort(myArr))
