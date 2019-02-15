""" create a Hash table, nums -> dict
Example:
      Input: nums = [2, 7, 1, 5]
	  Return: table = {2:0, 7:1, 1:2, 5:3}
 """
def createHashTable(nums):
	table = {}
	for i in range(len(nums)):
		table[nums[i]] = i
	return table


""" Two-pass Hash table """
def twoSum(nums, target):
	table = createHashTable(nums)
	for i in range(len(nums)):
		if target - nums[i] in table:
			return [i, table[target-nums[i]]]
	return 


""" One-pass Hash table """
def twoSumOnePass(nums, target):
	table = createHashTable(nums)
	for i, num in enumerate(nums):
		if target - num in table:
			return [i, table[target-num]]
			break
		# table[num] = i
	return ([])



if __name__ == "__main__":
	nums = [2,5,1,7]
	result = twoSumOnePass(nums, 9)
	# result2 = twoSum(nums, 9)
	print(result)
	# print(result2)


