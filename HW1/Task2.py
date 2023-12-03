# Задача №2
# Написать точно такую же процедуру(сортировка чисел в списке в порядке убывания), но в декларативном стиле

def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

numbers = [13, 22, 5, -9, 0]
print("Не сортированный список: ", numbers)

sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания: ", sorted_numbers)  # [22, 13, 5, 0, -9]