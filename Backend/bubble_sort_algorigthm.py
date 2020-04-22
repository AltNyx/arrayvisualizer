def bubble_sort(arr, size):
    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    nums = [x for x in range(20, 0, -1)]
    sorted_arr = bubble_sort(nums, len(nums))
    print(sorted_arr)