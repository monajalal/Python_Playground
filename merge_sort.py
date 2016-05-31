def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)/2
    first_list = merge_sort(list[:mid])
    second_list = merge_sort(list[mid:])
    return merge(first_list, second_list)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if (left[0] < right[0]):
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

int_list = [3, 4, 1, 20, 2, 4]

for item in merge_sort(int_list):
    print(item)
