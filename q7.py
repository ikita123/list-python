list=[[78,76,94,86,88],[91,71,98,65,76],[95,45, 78,52,49]]
i=0
sum=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum+=list[i][j]
        j=j+1
    i=i+1
print(sum)    