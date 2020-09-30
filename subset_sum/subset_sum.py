from typing import List


def check_sum(numbers: List[int], target_value: int):
    length = len(numbers)
    enumeration = list(enumerate(numbers))
    for i in range(0, 2 ** length):
        subset = [num for idx, num in enumeration if i & (1 << idx)]
        if sum(subset) == target_value:
            return subset
    return None
