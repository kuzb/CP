from typing import List


# standard binary search
def binarySearch(ls: List[int], target: int) -> int:
    left = 0
    right = len(ls) - 1
    while left <= right:
        # to prevent overflow with large indexes
        mid = left + (right - left) // 2
        if ls[mid] == target:
            return mid
        if ls[mid] < target:
            # move right
            left = mid + 1
        else:
            # move left
            right = mid - 1
    return -1


"""
Reasoning about binary search in terms of its applications:

BS can be used when problem we are tackling has list of values that can be
thought of as true and false relative to our problem solution. Then BS can
be used to move towards truest or falsest value by possibly changing direction
in each step of the execution.
"""


# find __first__ value equal or greater than the target
def findFVEG(ls: List[int], target: int) -> int:
    left = 0
    right = len(ls) - 1
    possible_answer = -1
    while left <= right:
        mid = left + (right - left) // 2

        if ls[mid] >= target:
            # saving it as possible answer, and each time
            # it's gets updated it is a better answer than
            # previous
            possible_answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return possible_answer


# find minimum number in shifted sorted list
# find minimum shift sorted list
def findMSSL(ls: List[int]):
    if len(ls) == 0:
        return -1
    if len(ls) == 1:
        return ls[0]

    left = 0
    right = len(ls) - 1

    if ls[left] < ls[right]:
        return ls[left]

    while left <= right:
        mid = left + (right - left) // 2

        # start of shift(i.e. smallest element) is exact right to mid
        if ls[mid] > ls[mid + 1]:
            return ls[mid + 1]

        # start of shift(i.e. smallest element) is exactly mid
        if ls[mid] < ls[mid - 1]:
            return ls[mid]

        # trying to move towards start of rotation i.e. where the smallest
        # element lies, and furthermore we are interested in right of rotation
        # index
        if ls[right] > ls[left]:
            # moving towards left, because list seems to be in correct order
            # i.e. smallest elements lies towards left
            right = mid - 1
        else:
            # moving towards right
            left = mid + 1


# find the maximum value in increases and then decreases list
# find maximum increasing decreasing list
def findMIDL(ls: List[int]):
    # We are meant to find index of change
    # values to left of index of change are considered false,
    # values to right of index of change are considered true,
    # so we can apply binary search

    if len(ls) == 0:
        return -1
    if len(ls) == 1:
        return ls[0]

    left = 0
    right = len(ls) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if ls[mid] > ls[mid - 1] and ls[mid] > ls[mid + 1]:
            return ls[mid]

        if ls[left] > ls[right]:
            # go to left
            right = mid - 1
        else:
            # go to right
            left = mid + 1


# find square root to some precision
def findSQRT(num: int, precision: float):
    left = 0
    right = num
    mid = 0

    while right - left > precision:
        # not rounding
        mid: float = left + (right - left) / 2

        if mid*mid > num:
            # move to left
            right = mid
        else:
            # move to right
            left = mid
    return mid
