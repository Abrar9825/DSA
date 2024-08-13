arraytobeSort=[65,34,98,23,43,35]
n=len(arraytobeSort)

for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if arraytobeSort[min_index] > arraytobeSort[j]:
            min_index=j
            
    arraytobeSort[i], arraytobeSort[min_index] = arraytobeSort[min_index], arraytobeSort[i]
    
    
print("Sorted Array",arraytobeSort)