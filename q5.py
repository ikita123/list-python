num=[5,6,7,8,9,1]
length=len(num)
small=num[0]
i=0
while i<length:
    if num[i]<small:
        small=num[i]
        i=i+1
print(small)