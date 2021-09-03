list=[1,2,3,4,5,20,30,50,45]
i=0
for i in range(i, len(list)):
    for j in range(i+1,len(list)):
        if (list[i]>list[j]):
            a=list[i]
            list[i]=list[j]
            list[j]=a
print(list)
