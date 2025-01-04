# dict = {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 6, 'b': 7, 'C': 8}
lst = list(map(int, input().split()))
if lst == sorted(lst):
    print('ascending')
elif lst == sorted(lst, reverse=True):
    print('descending')
else:
    print('mixed')