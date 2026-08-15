lst = []
n = int(input())

for _ in range(n):
    command = input().split()
    op = command[0]
    
    if op == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif op == "print":
        print(lst)
    elif op == "remove":
        lst.remove(int(command[1]))
    elif op == "append":
        lst.append(int(command[1]))
    elif op == "sort":
        lst.sort()
    elif op == "pop":
        lst.pop()
    elif op == "reverse":
        lst.reverse()
