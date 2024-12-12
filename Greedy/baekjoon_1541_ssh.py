equation = input()

equation_split = equation.split('-')
res = [ 0 ] * len(equation_split)
for idx, equation in enumerate(equation_split):
    equation_plus = list(map(int, equation.split('+')))
    res[idx] = sum(equation_plus)

ans = res[0]
for i in range(1, len(res)):
    ans -= res[i]

print(ans)