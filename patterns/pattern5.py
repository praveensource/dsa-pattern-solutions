# priniting  stars in reverse order and maintaining n values in each row and also decrementing down 
def stars(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print("*",end=" ")
        print()
        
stars(5)