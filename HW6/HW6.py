# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Пример использования
arr = [2, 4, 8, 12, 16, 20, 30]
target = 20

result = binary_search(arr, target)
if result != -1:
    print("Элемент найден в позиции", result)
else:
    print("Элемент не найден")