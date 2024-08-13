# [65,34,98,23,43,35]

arraytobeSort=[65,34,98,23,43,35]
n=len(arraytobeSort)
for i in range(0,n-1):
    for j in range(n-i-1):
        if arraytobeSort[j] > arraytobeSort[j+1]:
            arraytobeSort[j] , arraytobeSort[j+1]=arraytobeSort[j+1],arraytobeSort[j]
            
print(arraytobeSort)
            