n = int(input())

# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(1, n-1):
#         for j in range(i+1, n):
#             for k in range(j+1, n+1):
#                 sum += A[i]*A[j]*A[k]

# 3~7,4~7,..,7/4~7,..,7/../7 >> 1*5+2*4+..+5*1 >> sum(k)(6-k) >> sum(6k)-sum(k^2)
# 6*(5+1)(5)//2 - 5(5+1)(2*5+1)//6
# 일반화: sum(k)(n-k-1) = (n-1)*sum(k) - sum(k^2)
# (n-1)(n-1)(n-2)//2 - (n-2)(n-1)(2(n-2)+1)//6 = (n-1)(n-2)/6{3(n-1)-(2n-3)} = (n-1)(n-2)n//6

print((n-1)*(n-2)*n//6)
print(3)