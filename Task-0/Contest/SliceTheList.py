t = int(input())
for i in range(t):
    n = int(input())
    arr = input().split()
    for j in range(n):
        arr[j] = int(arr[j])
    for j in range(n):
        print(arr[n-j-1], end=" ")
    print("\n", end="")
    for j in range(1, n):
        if j % 3 == 0:
            print(str(arr[j]+3), end=" ")
    print("\n", end="")
    for j in range(1, n):
        if j % 5 == 0:
            print(arr[j]-7, end=" ")
    print("\n", end="")
    s = 0
    if n > 4:
        for j in range(3, 8):
            s+=arr[j]
    print(s)
