t=int(input())
while(t!=0):
    s=input().split(" ")
    counts=""
    for i in s:
        c=0
        for j in i:
            if(j=='@'):
                continue
            else:
                c+=1
        counts+= str(c)
        counts+=","
    print(counts[:len(counts)-1])
    t-=1
