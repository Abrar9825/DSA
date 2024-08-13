import time

start=time.perf_counter()
arraytobeSort=[65,34,98,23,43,35]

n=len(arraytobeSort)
for i in range(1,n):
    current_value=arraytobeSort[i]
    j = i -1
    
    while j >=0 and arraytobeSort[j]  > current_value:
        arraytobeSort[j+1]=arraytobeSort[j]
        j-=1
        
    arraytobeSort[j+1]=current_value
    
print(arraytobeSort)

end=time.perf_counter()

print(end-start)