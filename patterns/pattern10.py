'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
def stars(n):
    # top
    for i in range(1, n +  1):
        for j in range(i):
            print("*",end= " ")
        print()
            
    # bottom
    for i in range(n - 1, -1, -1):
        for j in range(i):
            print("*", end = " ")
        print()
stars(5)