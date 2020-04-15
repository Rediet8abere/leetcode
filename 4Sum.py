def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        four_sum = set()
        nums = sorted(nums)
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                low = j+1
                high = len(nums)-1
                while low < high:
                    sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if sum == target:
                        four_sum.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                        high -= 1
                    elif sum < target:
                        low += 1
                    else:
                        high -= 1
        print("four_sum: ", four_sum)

fourSum([-3,-2,-1,0,0,1,2,3], 0)
