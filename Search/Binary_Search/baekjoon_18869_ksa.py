import sys
from collections import defaultdict
from bisect import bisect_left
input = sys.stdin.readline

M, N = map(int, input().split())
pattern_count = defaultdict(int)

for _ in range(M):
    planets = list(map(int, input().split()))

    enum_planets = [(val, idx) for idx, val in enumerate(planets)]

    sorted_vals = sorted(x[0] for x in enum_planets)
    
    pattern = [0] * N
    prev_val = sorted_vals[0]
    curr_rank = 0
    
    for val, idx in enum_planets:
        pos = bisect_left(sorted_vals, val)

        if val != prev_val:
            curr_rank = pos
            prev_val = val
        pattern[idx] = curr_rank
    
    pattern_count[tuple(pattern)] += 1

result = sum(count * (count - 1) // 2 for count in pattern_count.values())
print(result)

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# M, N = map(int, input().split()) #우주의 개수 M과 각 우주에 있는 행성의 개수 N
# pattern_count = defaultdict(int)

# for _ in range(M):#각 우주에서
#     planets = list(map(int, input().split())) #행성 입력받음 1 1 2 6 8

#     enum_planets = [(val, idx) for idx, val in enumerate(planets)]#(값, 인덱스)
#     enum_planets.sort() 
#     #print(enum_planets) #[(1, 0), (1, 1), (2, 2), (6, 3), (8, 4)]
    
#     ranks = [0] * N
#     rank = 0
#     prev_val = enum_planets[0][0]
    
#     for i, (val, idx) in enumerate(enum_planets): #[0(1, 0), 1(1, 1), 2(2, 2), 3(6, 3), 4(8, 4)]
#         if val != prev_val:  # 값이 달라질 때만 rank 증가
#             rank = i
#             prev_val = val
#         ranks[idx] = rank
    
#     pattern_count[tuple(ranks)] += 1
#     print(pattern_count)

# result = sum(count * (count - 1) // 2 for count in pattern_count.values())
# print(result)