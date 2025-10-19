import pandas as pd
import numpy as np
from itertools import combinations

capacity = 10
def get_csv_data (filepath):
    df = pd.read_csv (filepath)
    return df


# | Item   | Weight | Value |
# |--------|--------|-------|
# | Item 1 | 2      | 3     |
# | Item 2 | 3      | 4     |
# | Item 3 | 4      | 5     |
# | Item 4 | 5      | 6     |


## Capacity is 10, challenge minimum weight , maximum value




def find_sum(nums, target, path=[]):
    if sum(path) == target:
        print("Combination found:", path)
        return True
    if not nums:
        return False

    # Include first number
    if find_sum(nums[1:], target, path + [nums[0]]):
        return True
    # Skip first number
    if find_sum(nums[1:], target, path):
        return True

    return False


def get_knapsack_bruteForceCombo (filepath):
    df = get_csv_data(filepath)
    weights = df.Weight.tolist()
    values = df.Value.tolist()
    weight_values_tuple = list(zip(weights, values))
    numbers = []
    for t in weight_values_tuple:
        numbers.append(t[0])
    find_sum(numbers, capacity)
    n = len(weights)
    return numbers


print(get_knapsack_bruteForceCombo("knapsack_dataset.xls"))
