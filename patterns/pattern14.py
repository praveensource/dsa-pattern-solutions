'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''
def pattern14(N):
    # Outer loop for rows
    for i in range(N):
        # Inner loop: print alphabets from 'A' to 'A'+i
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=" ")
        # Move to next line
        print()

if __name__ == "__main__":
    N = 5
    pattern14(N)
