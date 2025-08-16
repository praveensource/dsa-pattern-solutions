'''
A B C D E 
A B C D 
A B C 
A B 
A 
'''
def pattern15(N):
    # Outer loop for rows
    for i in range(N - 1, -1, -1):
        # Inner loop: print alphabets from 'A' to 'A'+i
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=" ")
        # Move to next line
        print()

if __name__ == "__main__":
    N = 5
    pattern15(N)
