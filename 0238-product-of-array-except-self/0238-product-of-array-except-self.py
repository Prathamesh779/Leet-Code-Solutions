class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        leftproducts = [1] * n
        rightproducts = [1]* n
        result = [0] * n

        for i in range(1, n):
            leftproducts[i] = leftproducts[i - 1] * nums[i - 1]
        
        for i in range(n-2,-1,-1):
            rightproducts[i] = rightproducts[i+1] * nums[i + 1]
            
        for i in range(n):
             result[i] = leftproducts[i] * rightproducts[i]

        return result
    



    