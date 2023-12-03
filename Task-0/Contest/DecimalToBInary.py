b=""
while(n!=0):
    b=b+str(n%2)
    n=n/2
while(len(b)<8):
    b+="0"
bin_num = b[:-1]
