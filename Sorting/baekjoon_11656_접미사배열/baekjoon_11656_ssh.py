S = input()

words = [ S[i:len(S)] for i in range(0, len(S)) ]
words.sort()

print('\n'.join(words))