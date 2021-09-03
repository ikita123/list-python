num=[50,40,23,56,12,5,10,7]
i=0
count=num[i]
while i<len(num):
    j=num[i]
    if j>count:
        count=j
    i=i+1
print(count,"maximum")
