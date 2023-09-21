# Hash Function

# ord() function returns the character's number.
# ord("b") -- > 98 in ASCII
print(ord("b"))
# Python has its own hash function at the background named hash()
# that turns input to some number according to function

# Same input will return same output from hash function.
# and if I get mode of that output with 8, then it'll be giving the same result.
# then it will place the value the place where result is.
print(hash("apple") % 8)
print(hash("apple") % 8)


# For example; we write a hash funtion on our own.
def hashFunction(key):
    myHash = 0
    for letter in key:
        myHash = (myHash + ord(letter) * 19)
    return myHash


print(hashFunction("apple"))
print(hashFunction("appl"))


# Another Hash function from other sources

def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), 1)
    )


print(hash_function("apple"))


class HashTable:
    def __init__(self, size=13):
        self.dataMap = [None] * size  # 13 tane içi boş bir liste olacak ilk başta

    def hashFuntion(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)
        return myHash

    def setItem(self, key, value):
        index = self.hashFuntion(key)
        if self.dataMap[index] is None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])  # key ve value yu birlikte katdediyorum, yani [apple, 200] gibi.

    def getItem(self, key):
        index = self.hashFuntion(key)
        if self.dataMap[index] is not None:
            for i in range(len(self.dataMap[index])):
                if self.dataMap[index][i][0] == key:
                    return self.dataMap[index][i][1]
        return None

    def getKeys(self):
        keys = []
        for i in range(len(self.dataMap)):
            if self.dataMap[i] is not None:
                for j in range(len(self.dataMap[i])):
                    keys.append(self.dataMap[i][j][0])
        return keys

    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, "-> ", value)

print("-----------")
hashTable = HashTable()
hashTable.setItem("Apple", 100)
hashTable.setItem("Banana", 150)
hashTable.setItem("Melon", 250)
hashTable.setItem("Strawberry", 300)
hashTable.setItem("WaterMelon", 100)
hashTable.setItem("Lemon", 150)

hashTable.printTable()

print("----------------")

print(hashTable.getItem("Lemon"))
print(hashTable.getItem("Melon"))

print(hashTable.getKeys())