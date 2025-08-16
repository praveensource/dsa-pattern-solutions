'''
       *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
'''
def stars(n):
    for i in range(n):
        # printing spaces
        for j in range(n - i - 1):
            print(" ", end = " ")
        # printing stars
        for j in range(2 * i + 1):
            print("*",end=" ")
        # printing spaces
        for j in range(n - i - 1):
            print(" ", end = " ")
        print()
        
stars(5)