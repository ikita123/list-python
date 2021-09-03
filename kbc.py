print("WEL COME IN KBC")
q=["how many continents are there","what is the capital of india","ng mei kaun se course padaya jaata hai"]
o=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software","2.counseling","3.tourism","4.agriculture"]]
s=[3,4,1]
m=0
n=1
c=0
for i in range(0,len(q)):
    print(q[i])
    for j in range(0,len(o)+1):
        print(o[i][j])
    f=["3. seven","4. eight","2.bhopal","4.delhi","1.softwear","2.counseling"]
    print('you have 50-50 life line')
    num=input("do you want life line, yes or not")
    if num=="yes":
        if c==0:
            print(f[i+m])
            print(f[i+n])
            n=int(input("enter answer"))
            if s[i]==n:
                print("your answer is right") 
                c+=1
            else: 
                print("wrong")
                break
        else:
            print("you have already taken lifeline")
            p=int(input("enter correct answer"))
            if s[i]==p:
                print("right")
            else:
                print("wrong")
                break
    elif num=="no":
        t=int(input("enter answer"))
        if s[i]==t:
            print("right")
        else:
            print("wrong")
            break
    else:
        print("wrong")
        break
    m+=1
    n+=1