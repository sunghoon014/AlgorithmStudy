N = int(input())
guitars = [input() for _ in range(N)]
guitars.sort(key=lambda x:(len(x), sum([int(str) for str in x if ord('0')<=ord(str)<=ord('9')]), x))
for num in guitars: print(num)