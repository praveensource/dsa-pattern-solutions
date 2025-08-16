# priniting  stars in rows and columns by incrementing star in each rows
def stars(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*",end=" ")
        print()
        
stars(5)