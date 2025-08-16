'''
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
'''
def solve(n):
    spaces = 2 * (n - 1)
    for i in range(1, n + 1):
        # number
        for j in range(1, i+ 1):
            print(j, end= " ")
        # spaces
        for j in range(spaces):
            print(" ", end= " ")
        # number
        for j in range(i, 0, -1):
            print(j, end= " ")
        spaces -= 2
        print()

solve(5)