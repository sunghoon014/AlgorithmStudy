while True:
    try:
        print(sum(map(int, input().split())))
    except EOFError:
        break

# while True:
#     data = input()
#     if not data:
#         break
#     print(sum(map(int, data.split())))