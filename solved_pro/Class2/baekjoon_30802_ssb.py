n = int(input())
t_shirts = list(map(int, input().split()))
t, p = map(int, input().split())

min_t = sum(map(lambda x: (x-1)//t+1 if x else 0, t_shirts))
max_p = divmod(n, p)
print(min_t)
print(*max_p)