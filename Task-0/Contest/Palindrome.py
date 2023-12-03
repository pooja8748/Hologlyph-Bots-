t = int(input())
while(t!=0):
    s= input()
    s=s.upper()
    rs=s[: :-1]
    if(s==rs):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
    t -= 1 
