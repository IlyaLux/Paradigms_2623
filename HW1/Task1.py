# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers = [13, 22, 5, -9, 0]
print("Не отсортированный список: ", numbers)

sorted_numbers = sort_list_imperative(numbers)
print("Отсортированный список в порядке убывания: ", sorted_numbers)  # [22, 13, 5, 0, -9]