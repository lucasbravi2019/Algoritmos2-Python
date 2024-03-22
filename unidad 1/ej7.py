from typing import List

def find_first_numbers(numbers: List[int], first_numbers: List[int], numbers_quantity: int) -> None:
    numbers_size: int = len(numbers)

    if numbers_size >= 1 and numbers_quantity >= 1:
        actual_digit: int = numbers.pop(0)
        first_numbers.append(actual_digit)
        find_first_numbers(numbers, first_numbers, numbers_quantity - 1)

first_numbers: List[int] = []
numbers: List[int] = [1, 2, 5, 6, 7, 8, 9, 122, 32, 12333]
numbers_quantity: int = 10

find_first_numbers(numbers, first_numbers, numbers_quantity)

print(first_numbers)
