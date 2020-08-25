def difference(N):

    # Calculates using the sum of consecutive integers and sum of squares formulas
    print(int((N*(N+1)/2)**2 - N*(N+1)*(2*N+1)/6))

test_cases = int(input())
for i in range(test_cases):
    N = int(input())
    difference(N)