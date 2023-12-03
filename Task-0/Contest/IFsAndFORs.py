t= int(input())
while (t!=0):
    n= int(input())
    s=""
    for i in range (0,n,1):
        if(i==0):
            s=s+'3'+" "
        else:
            if(i%2==0):
                s=s+str(2*i)+" "
            else:
                s=s+str(i*i)+" "
    s.strip()
    print(s)
    t-=1
