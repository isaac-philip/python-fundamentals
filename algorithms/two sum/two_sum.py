"""
    Given array of integers,
    find 2 consecutive index which sum returns target Integer number

    https://leetcode.com/problems/two-sum/

    Example run,

        Please input list of numbers separated by space :
        10 20 30 40
        Please input the Target number :
        70
        Found! :-)
        [2, 3]
        
"""

from typing import List

def calculate_target_sum(lst_nums: List[int], target: int) -> List[int]:
    """
        Find out the list of indices for the array items
            whose sum equate to the target
    :param lst_nums: List of numbers
    :param target: The target number
    :return:
    """
    map_nums_to_check = dict()
    output_lst = []
    for idx, num in enumerate(lst_nums):
        target_diff = target - num
        if target_diff in map_nums_to_check:
            output_lst = [map_nums_to_check[target_diff], idx]
            break
        else:
            map_nums_to_check.update({num:idx})
    return output_lst

def accept_input():
    print("Please input list of numbers separated by space :")
    input_nums = input()
    print("Please input the Target number :")
    target = int(input())
    numbers_str = input_nums.split(" ")
    numbers  = list(map(lambda x : int(x), numbers_str))
    output = calculate_target_sum(numbers, target)
    if output:
        print("Found! :-)")
        print(output)
    else:
        print("Not Found! :-(")


if __name__ ==  "__main__":
    accept_input()