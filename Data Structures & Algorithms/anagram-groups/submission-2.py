class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        result = []

        count = 0
        for i in range(len(strs)):
            ss = ''.join(sorted(strs[i]))
            if ss not in dt:
                dt[ss]  = count
                result.append([strs[i]])
                count += 1
            else:
                result[dt[ss]].append(strs[i])
        return result