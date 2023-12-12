n = 7 
array = [[0 for i in range(n)] for j in range(n)] 

for i in range(n):
    for j in range(n): 
        if i + j < n: 
            array[i][j] = n - i - j 

for i in range(n): 
    for j in range(n): 
        print(array[i][j], end=" ") 
    print() 