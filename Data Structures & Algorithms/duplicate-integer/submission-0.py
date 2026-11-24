class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        flag = False

        for i in nums:
            if i not in dup:
                dup[i] = 0
            else:
                flag = True 
                break
        return flag