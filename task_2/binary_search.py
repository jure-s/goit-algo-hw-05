def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None

    return (iterations, upper_bound)

# Тестування
if __name__ == "__main__":
    sorted_arr = [1.2, 2.5, 3.8, 4.4, 5.9, 7.1]
    print(binary_search_with_upper_bound(sorted_arr, 3.8))  # (кількість ітерацій, 3.8)
    print(binary_search_with_upper_bound(sorted_arr, 6.0))  # (кількість ітерацій, 7.1)
    print(binary_search_with_upper_bound(sorted_arr, 0.5))  # (кількість ітерацій, 1.2)
    print(binary_search_with_upper_bound(sorted_arr, 8.0))  # (кількість ітерацій, None)
