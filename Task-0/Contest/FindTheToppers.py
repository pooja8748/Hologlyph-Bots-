T = int(input(""))
for i in range(T):
    n = int(input(""))
    names = []
    marks = []
    str = ""
    for j in range(n):
        str = input("").split()
        names.append(str[0].lower())
        marks.append(float(str[1]))

    ans = 0
    toppers = []
    maxmarks = -1
    for j in range(n):
        if marks[j] > maxmarks:
            maxmarks = marks[j]
            toppers = [names[j]]
        elif marks[j] == maxmarks:
            toppers.append(names[j])
    toppers.sort()
    for topper in toppers:
        print(topper[0].upper() + topper[1:len(topper)])
