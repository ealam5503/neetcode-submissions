class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for idx, char in enumerate(s):
            if char not in s_dict:
                s_dict[char] = 0
            s_dict[char] += 1

            if t[idx] not in t_dict:
                t_dict[t[idx]] = 0 
            t_dict[t[idx]] += 1

        return s_dict == t_dict