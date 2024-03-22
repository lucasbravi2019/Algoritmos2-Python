from typing import List

def digitos(numbers: int) -> List[str]:
    digits: List[str] = []
    allnumbers: str = str(numbers)
    for number in allnumbers:
        digits.append(number)

    return digits


print(digitos(11561))