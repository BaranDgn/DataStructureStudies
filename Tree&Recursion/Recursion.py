#Recursion

# Factorial is one of the problem we can use recursive to solve.



def calculateFactorial(num):
    # edge case : uç nokta(yada uç ornek),
    # factorial orneginde edge case 0 dır.
    # 0! = 1 dir. eger bize 0 factorial verilirse her durumda 1 döndürmeliyiz.
    # aynı zamanda bu bizim exit case mizde olacak.

    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num - 1)  # kendi fonksiyonun kendi içinde bir daha cağırdı.
                                                  # işte recursive budur. Başka bir örnekler kendini tekrarlama dır.
                                                  # Aynı zamanda num = 0 oldugunda da bu işlemi bitirebildik aksi halde sonsuza kadar gidecekti.


def calculateContigiousSum(num):
    if num == 0:
        return 0
    else:
        return num + calculateContigiousSum(num - 1)