def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    nums = [x for x in range(20, 0, -1)]
    sorted_arr = insertion_sort(nums, len(nums))
    print(sorted_arr)