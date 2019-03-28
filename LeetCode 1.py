"""Create a Hash table.  list -> dict
Example:
    Input: nums = [2, 7, 1, 6]
    Return: table = {2:0, 7:1, 1:2, 6:3}
"""

""" Two-Pass Hash Table. """
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
       if target - nums[i] not in d:
           d[nums[i]] = i
       else:
            return [d[target - nums[i]], i]



if __name__ == "__main__":
    nums = [2, 5, 1, 1]
    result = twoSumOnePath(nums, 7)
    print(result)

