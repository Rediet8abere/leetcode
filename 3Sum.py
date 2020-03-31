def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        threesum = []

        if len(nums)==0 or nums==None:
            return threesum
        nums = sorted(nums)
        print("nums", nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                    print("to pass", nums[i], nums[i-1])
                    continue
            left = i+1
            right = len(nums)-1
            while left<right:
                sum = nums[left]+nums[right]+nums[i]
                print("sum", sum)
                print(nums[left], nums[right], nums[i])
                if sum<0:
                    left+=1
                elif sum<right:
                    right-=1
                else:
                    threesum.append([nums[left], nums[right], nums[i]])
                    while left<right and nums[left]==nums[left+1]:
                        left = left + 1
                    while left<right and nums[right]==nums[right-1]:
                        right = right + 1
                    left+=1
                    right-=1
        return threesum



print(threeSum([-1, 0, 1, 2, -1, -4]))
