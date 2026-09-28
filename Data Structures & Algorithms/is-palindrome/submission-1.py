class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        alphanumeric = set('abcdefghijklmnopqrstuvwxyz0123456789')
        s_list = list(filter(lambda char: char.lower() in alphanumeric, list(s)))

        i, j = 0, len(s_list) - 1

        while i <= j:
            if s_list[i].lower() not in alphanumeric:
                i += 1
            if s_list[j].lower() not in alphanumeric:
                j -= 1
            if s_list[i].lower() != s_list[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
