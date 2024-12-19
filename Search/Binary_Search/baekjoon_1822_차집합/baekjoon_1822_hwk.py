from bisect import bisect_left, bisect_right

num_A, num_B = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))
setA.sort()
setB.sort()

answer = 0
answers = []
for element in setA:
        if bisect_left(setB, element)==bisect_right(setB, element):
                answer+=1
                answers.append(element)
if answer:
        print(answer)
        print(*answers)
else:
        print(0)
