def prime_factor(N):
    factor = 2
    while factor * factor <= N:
        if N % factor == 0:
            N /= factor
        else:
            factor += 1
    print(int(N))


test_cases = int(input())
for i in range(test_cases):
    N = int(input())
    prime_factor(N)