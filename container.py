def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = -2147483648 #minValue
        area = 0
        i = 0
        j = len(height)-1
        while i<j:
            if height[i] < height[j]:
                area = height[i]*(j-i)
                i+=1
            else:
                area = height[j]*(j-i)
                j-=1
            if area > maxarea:
                maxarea = area

        return maxarea

print(maxArea([1,8,6,2,5,4,8,3,7]))
