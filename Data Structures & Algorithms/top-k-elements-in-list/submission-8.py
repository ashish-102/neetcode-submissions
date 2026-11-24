class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dt = {}
        result = []

        for n in nums:
            if n not in dt:
                dt[n] = 1
            else:
                dt[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for ky, v in dt.items():
            bucket[v].append(ky)

        for i in range(len(bucket)-1, -1 , -1):
            if not bucket[i]:
                continue
            if bucket[i]:
                result.extend(bucket[i])

            if len(result) == k:
                break

        return result