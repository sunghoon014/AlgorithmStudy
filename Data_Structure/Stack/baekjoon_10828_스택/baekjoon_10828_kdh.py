# 10828 스택
tong=[]

def push(X):
    tong.append(X)

def pop():
    if len(tong)==0:
        print(-1)
    else:
        popped_X=tong.pop()
        print(popped_X)

def size():
    print(len(tong))

def empty():
    if len(tong)==0:
        print(1)
    else:
        print(0)

def top():
    if len(tong)==0:
        print(-1)
    else:
        print(tong[-1])

N=int(input())
for _ in range(N):
    command=input()
    if len(command.split())==2:
        func,x=command.split()
        push(int(x))
    else:
        func=command
        if func=="pop":
            pop()
        elif func=="size":
            size()
        elif func=="empty":
            empty()
        elif func=="top":
            top()