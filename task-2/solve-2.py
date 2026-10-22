n = int(input())
totalsum = 0
for _ in range(n):
    x = int(input())
    if x % 6 == 0 and x % 10 == 4:
        totalsum += x
print(totalsum)
