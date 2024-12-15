string = input()
list = sorted([string[i:] for i in range(len(string))])
for st in list:
    print(st)