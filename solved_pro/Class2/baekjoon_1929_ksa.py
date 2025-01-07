M, N = map(int, input().split())

def miller_rabin(n, a): #n은 판별할 숫자, a는 2, 3(소수)
    if n == a:
        return True
    if n % 2 == 0: #짝수는 2빼면 다 합성수임
        return False
    
    # n-1 = 2^s * d 형태로 분해
    d = n - 1 #홀수
    while d % 2 == 0: #d가 짝수면 계속 2로 나눠줌 (2^s)
        d //= 2 # a^d 이 -1 (mod n)인 경우 소수일 확률
        if pow(a, d, n) == n-1:
            return True
        
    x = pow(a, d, n)
    if x == 1 or x == n-1: #x가 1 또는 n-1이면(=-1) 소수일 확률
        return True
        
    return False

def is_prime(n):
    if n <= 1:
        return False
        
    for a in [2, 3]:
        if not miller_rabin(n, a):
            return False
    return True

for i in range(M, N + 1):
    if is_prime(i):
        print(i)