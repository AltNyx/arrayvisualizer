def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    nums = [x for x in range(20, 0, -1)]
    sorted_arr = selection_sort(nums, len(nums))
    print(sorted_arr)