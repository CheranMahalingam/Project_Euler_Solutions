def prime(N):
    primes_ordered = [2]
    current = 3
    total_primes = 1
    while total_primes < N:
        for i in range(total_primes):
            if current % primes_ordered[i] == 0:
                current += 1
                break
            elif i == total_primes - 1:
                total_primes += 1
                primes_ordered.append(current)
                current += 1
    return primes_ordered


test_cases = int(input())
prime_list = prime(10000)

for i in range(test_cases):
    N = int(input())
    print(prime_list[N - 1])
