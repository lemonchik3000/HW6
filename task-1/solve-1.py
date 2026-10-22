# TODO: Вставить сюда код задачи 1.
count = int(input())
total_sum = 0

for _ in range(count):
    num = int(input())
    if num % 10 == 3:
        total_sum += num

print(total_sum)
