
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        # print(middle)

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print('Sorted: ' + str(arr))


test_array = [5, 2, 4, 7, 1, 3, 2, 6]

print('Test array before: ' + str(test_array))
merge_sort(test_array)
print('Test array after: ' + str(test_array))