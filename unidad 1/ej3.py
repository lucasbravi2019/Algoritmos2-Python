from typing import List

def average(numbers: List[int]) -> float:
    sum: float = 0
    for number in numbers:
        sum += number

    return sum / len(numbers)

numbers: List[int] = [3, 18, 17, 44, 14, 12, 29, 19, 4, 6, 17, 7, 14, 6, 8, 17, 17, 21, 65,
      19, 10, 31, 92, 17, 5, 15, 3, 14, 20, 12, 29, 57, 15, 2, 17, 1, 6, 17, 2,
      71, 12, 11, 62, 14, 9, 20, 43, 19, 4, 15,5]

print(average(numbers))