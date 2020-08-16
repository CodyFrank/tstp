# Given a non-empty list of integers, every element appears twice except for one. Find that single one.
list1 = [1, 1, 2, 2, 3, 4, 4, 5, 5]
count = {}

for i in list1:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for key, value in count.items():
    if value == 1:
        print(key)