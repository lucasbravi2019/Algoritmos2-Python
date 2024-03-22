from typing import List

def fill_array(num: int, numbers: List[int], position: int) -> None:
    initial_position: int = position * 100
    limit: int = initial_position + 100
    for i in range(initial_position, limit):
        numbers[i] = num

numbers: List[int] = [0] * 300
position: int = 0

fill_array(-1, numbers, position)
position += 1
fill_array(0, numbers, position)
position += 1
fill_array(1, numbers, position)

print(numbers)