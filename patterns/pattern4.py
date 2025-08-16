# priniting  numbers in rows and columns with same number in a row until the given range
def stars(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i,end=" ")
        print()
        
stars(5)