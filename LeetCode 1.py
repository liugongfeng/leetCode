"""Create a Hash table.  list -> dict
Example:
    Input: nums = [2, 7, 1, 6]
    Return: table = {2:0, 7:1, 1:2, 6:3}
"""
def createHashTable(nums):
    table = {}
    for i in range(len(nums)):
        table[nums[i]] = i
    return table

""" Two-Pass Hash Table. """
def twoSum(nums, target):
    table = createHashTable(nums)
    for i in range(len(nums)):
        if target - nums[i] in table:
            if table[target - nums[i]] != i:
                return [i, table[target - nums[i]]]
    return []


""" One-Pass Hash Table. """
def twoSumOnePath(nums, target):
    table = createHashTable(nums)
    for i, num in enumerate(nums):
        if target - num in table:
            return [i, table[target - num]]
    return []


if __name__ == "__main__":
    nums = [2, 5, 1, 1]
    result = twoSumOnePath(nums, 7)
    print(result)

