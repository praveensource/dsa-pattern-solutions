# priniting  numbers in reverse order and maintaining n values in each row and also decrementing as we go down
def stars(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print(j + 1,end=" ")
        print()
        
stars(5)