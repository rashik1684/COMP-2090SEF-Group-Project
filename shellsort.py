def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2
    return arr

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 5, 47, 19, 3]
    print("Original array:", numbers)
    shell_sort(numbers)
    print("Sorted array:  ", numbers)