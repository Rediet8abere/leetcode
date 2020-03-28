def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # threesum = []
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         for k in range(j, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 and nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!=nums[i]:
        #                 threesum.append([nums[i], nums[j], nums[k]])
        # return threesum

        threesum = []
        i = 0
        j = 1
        k = 2
        while i<len(nums)-1:
            print("In while", i, j, k)
            # -1, 0, 1, 2, -1, -4
            if i<len(nums) and j<len(nums) and k<len(nums):
                if nums[i]+nums[j]+nums[k]==0:
                    threesum.append([nums[i], nums[j], nums[k]])
            # 0,0,0,0
            # k loop
            if k<len(nums):
                k+=1
            # j loop
            elif j<len(nums)-1:
                if k==len(nums):
                    k=j+2
                j+=1
            # i loop
            elif i<len(nums)-1:
                if j==len(nums)-1:
                    j=i+2
                i+=1
        return threesum



print(threeSum([0,0,0,0]))
