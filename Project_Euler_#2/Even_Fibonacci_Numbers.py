def fibonacci(N):
    sum = 10
    temp1 = 8
    temp2 = 34
    while temp2 <= N:
        sum += temp2
        current = temp1
        temp1 = temp2
        temp2 = temp2*4 + current
    print(sum)

test_cases = int(input())
for i in range(test_cases):
    N = int(input())
    fibonacci(N)