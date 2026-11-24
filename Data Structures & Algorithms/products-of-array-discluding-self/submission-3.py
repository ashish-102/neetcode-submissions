class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pos = False
        soe = 1

        for  i in range(len(nums)):
            if nums[i]:
                soe *= nums[i] 
            else:
                pos += 1
            if pos > 1:
                soe = 0
                break 

        for j in range(len(nums)):
            if not nums[j]:
                nums[j] = soe
            else:
                nums[j] = soe // nums[j] if not pos else 0

        return nums