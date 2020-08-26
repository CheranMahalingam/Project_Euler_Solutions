from math import factorial

test_cases = int(input())
for i in range(test_cases):
    N, M = input().split()
    N, M = [int(N), int(M)]
    print(int(factorial(N + M) // (factorial(M)*factorial(N))) % (10**9 + 7))
