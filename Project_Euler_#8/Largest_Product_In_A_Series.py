def max_series(integer, digits, consecutive):
    placeholder = []
    for i in range(digits):
        placeholder.append(integer % 10)
        integer = integer // 10
    placeholder.reverse()
    max_product = 0
    for j in range(digits - consecutive + 1):
        current_product = 1
        for k in range(j, j + consecutive):
            current_product *= placeholder[k]
        if current_product > max_product:
            max_product = current_product
    print(max_product)


test_cases = int(input())
for i in range(test_cases):
    N, K = input().split()
    N, K = [int(N), int(K)]
    number = int(input())
    max_series(number, N, K)
