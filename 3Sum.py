def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        three_sum = set()
        for i in range(len(nums)):
            low = i+1
            high = len(nums)-1
            sum = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == sum:

                    three_sum.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] > sum:
                    high -= 1
                else:
                    low += 1
        return three_sum

print(threeSum([-1, 0, 1, 2, -1, -4, -1]))
