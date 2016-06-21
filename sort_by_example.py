'''
test.describe("Example Tests")
test.assert_equals(example_sort([1,2,3,4,5],[2,3,4,1,5]),[2,3,4,1,5])
test.assert_equals(example_sort([1,2,3,3,3,4,5],[2,3,4,1,5]),[2,3,3,3,4,1,5])

'''

def example_sort(arr, example_arr):
    # your code here
    sorted_arr = sorted(arr)
    result = []
    for item in example_arr:
        item_count=sorted_arr.count(item)
        for i in range(item_count):
            result.append(item)
    return result

print(example_sort([1,2,3,4,5],[2,3,4,1,5]))
print(example_sort([1,2,3,3,3,4,5],[2,3,4,1,5]))




def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum += num
    return sum

print(positive_sum([1,5,-5,-6,0,9]))