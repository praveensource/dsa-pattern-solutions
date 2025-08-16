# priniting  numbers in rows and columns increasing order in each rows
def stars(n):
    for i in range(n):
        for j in range(i+1):
            print(j + 1,end=" ")
        print()
        
stars(5)