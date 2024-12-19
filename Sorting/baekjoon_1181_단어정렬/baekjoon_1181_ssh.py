import sys

N = int(sys.stdin.readline())

words = [ sys.stdin.readline().strip() for i in range(N) ]
words = list(set(words))
words.sort(key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))