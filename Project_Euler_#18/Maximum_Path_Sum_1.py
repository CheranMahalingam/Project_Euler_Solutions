def best_path(row, previous):
    for i in range(len(row)):
        if i == 0:
            row[i] += previous[i]
        elif i == len(row) - 1:
            row[i] += previous[i-1]
        else:
            row[i] += max(previous[i-1], previous[i])


test_cases = int(input())
for i in range(test_cases):
    N = int(input())
    dp_row = []
    dp_previous = []
    for j in range(N):
        if j == 0:
            dp_row = list(map(int, input().split()))
            dp_previous = dp_row
        else:
            dp_previous = dp_row
            dp_row = list(map(int, input().split()))
            best_path(dp_row, dp_previous)
    print(max(dp_row))
