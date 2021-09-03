string=input("enter the string")
i=0
b=[]
for i in range(0,len(string)):
        if string[i]=="a"or string[i]=="e" or string[i]=="i" or string[i]=="o"or string[i]=="u":
            b.append(string[i])
        else:
            b.append(string[i])
for i in range(0,len(string)):
    for j in range(0,len(string)):
        if (b[i]<b[j]):
            f=b[i]
            b[i]=b[j]
            b[j]=f
print(b)