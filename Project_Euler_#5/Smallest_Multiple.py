def smallest_multiple(N, array):
    product = 1
    for m in range(N):
        product *= array[m]
    print(product)

test_cases = int(input())

# Array to store simplified terms for numbers 1 - 40
simplified_array = [i for i in range(1, 41)]

# Finds which prime factors remain for each integer
for j in range(2, 41):
    temp = j

    # Checks if current number is divisible by previous numbers in simplified_array
    # Removes already used prime factors
    for k in range(0, j-1):
        if temp % simplified_array[k] == 0:
            temp /= simplified_array[k]
    simplified_array[j - 1] = int(temp)

for i in range(test_cases):
    N = int(input())
    smallest_multiple(N, simplified_array)