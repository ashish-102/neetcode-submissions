class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sd = {}
        td = {}
        flag = True

        for i in s:
            if i not in sd:
                sd[i] = 1
            else:
                sd[i] = sd[i]+1

        for i in t:
            if i not in td:
                td[i] = 1
            else:
                td[i] = td[i]+1

        # print(sd, td)


        for k,v in sd.items():
            if k not in td or td[k] != v:
                flag = False
    
        return flag