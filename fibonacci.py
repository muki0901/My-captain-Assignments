nterm = int(input("Enter the number of terms: ")) #selecting number of terms
n1=0  
n2=1
next_val = 0
for x in range(0,nterm):  #reading each elements according to range
    next_val = n1+n2      
    n1=n2
    n2 = next_val
    print(n2)      #printing fibonacci series
    
    
    
    
    
