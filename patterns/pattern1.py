# priniting 5 stars in rows and columns
def stars(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*",end=" ")
        print()
        
stars(5)