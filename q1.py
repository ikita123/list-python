list1=[1,2,3.4,5,6,7,8,9]
list2=[10]
i=0
while i<len(list1):
    if list2 in list1:
        print("yes")
    else:
        print("no")
    i=i+1