class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dt = {}
        result = []

        for n in nums:
            if n not in dt:
                dt[n] = 1
            else:
                dt[n] += 1

        bucket = [ [] for i in range(len(nums)+1)]
        
        for ky, v in dt.items():
            bucket[v].append(ky)

        for i in range(len(bucket)-1, -1 , -1):
            if bucket[i]:
                result.extend(bucket[i])
            # print(i, result, len(result), len(result) == k)
            if len(result) == k:
                break
        return result