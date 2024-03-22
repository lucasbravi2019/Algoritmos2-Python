from typing import List

def reverse(numbers: List[int], reversed_numbers: List[int]) -> List[int]:
    numbers_size: int = len(numbers)

    if numbers_size >= 1:
        actual_digit: int = numbers.pop(numbers_size - 1)
        reversed_numbers.append(actual_digit)
        reverse(numbers, reversed_numbers)


numbers: List[int] = [1, 3, 1, 23, 5]
reversed_numbers: List[int] = []
reverse(numbers, reversed_numbers)

print(reversed_numbers)