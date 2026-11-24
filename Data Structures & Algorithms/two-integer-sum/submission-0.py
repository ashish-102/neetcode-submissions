class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rd = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if nums[i] not in rd:
                rd[rem] = i
            else:
                return [rd[nums[i]] , i]
        return [0, 0]