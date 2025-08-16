''''
A 
B B 
C C C 
D D D D 
E E E E E 
''''
def solve(n):
    
    for i in range(n):
        start = chr(ord("A") + i)
        for j in range(i + 1):
            print(start, end = " ")
        print()
solve(5)