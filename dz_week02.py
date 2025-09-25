print("Write numbers\n")
array = [int(i) for i in input().split()]
size = len(array)

start, end = 0, size - 1
max_s = 0

for i in range(0, size):
    S = (end - start) * min(array[start], array[end])
    max_s = S if max_s < S else max_s

    if (array[start] < array[end]): start += 1
    else: end -= 1

print(max_s)
