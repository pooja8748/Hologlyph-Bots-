from functools import reduce
t = int(input())
def series(a, d, n):
    ap = [a + (i * d) for i in range(n)]
    return ap
for i in range(t):
    str = input().split()
    a = int(str[0])
    d = int(str[1])
    n = int(str[2])
    s = series(a, d, n)
    for j in s:
        print(j, end=" ")
    print()
    sq = list(map(lambda x: x**2, s))
    for j in sq:
        print(j, end=" ")
    print()
    Sum = reduce(lambda x, y: x + y, sq)
    print(Sum)
