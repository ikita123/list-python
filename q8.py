number=30
n=[10,11,12,13,14,17,18,19]
i=0
b=-1
c=[]
length=len(n)
while i<length:
    m=n[i]
    a=n[b]
    s=m+a
    if s==number:
        b=b-1
        c.append([m,a])
    i+=1
print(c)