def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #-3
        # print("close? ", closest)
        # prev_dist = sum(nums[:3])
        # if the differnce between sum
        # the difference between closest and target
        # is smaller than element at index and taget then swap

        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total > target:
                    high -= 1
                else:
                    low += 1
                if abs(total-target) < abs(closest-target):
                    closest = total
                # ##############################################
                # distance = abs(total-target)
                # prev_dist = abs(closest-target)
                # if distance <= prev_dist:
                #     closest = total
                #     low += 1
                # elif distance > prev_dist:
                #     high -= 1



        return closest

print("closest: ", threeSumClosest([1,1,-1,-1,3], -1))
