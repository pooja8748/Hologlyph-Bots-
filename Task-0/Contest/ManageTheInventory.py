t = int(input())
for i in range(t):
    n = int(input())
    item = {}
    for j in range(n):
        s = input().split()
        item[s[0]] = int(s[1])

    m = int(input())
    for j in range(m):
        s = input().split()
        com = s[0]
        name = s[1]
        quantity = int(s[2])
        if(com == "ADD"):
            if item.get(name):
                item[name]+=quantity
                print("UPDATED Item " + name)
            else:
                item[name] = quantity
                print("ADDED Item " + name)
                n+=1
        elif(com == "DELETE"):
            if item.get(name):
                if(item[name] >= quantity):
                    item[name]-=quantity
                    print(f"DELETED Item {name}")
                else:
                    print(f"Item {name} could not be DELETED")
            else:
                print(f"Item {name} does not exist")
    
    s = 0
    for key in item.values():
        s += key
    print(f"Total Items in Inventory: {s}")
