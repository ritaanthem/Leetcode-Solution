'''
my solution:
time transcend 92.2%
memory transcend 45.95%
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_re = s[::-1]
        lenth = len(s)

        start = 0
        i = 1

        max_len = 0
        max_str = ""

        while start < lenth and i <= lenth:
            
            palindromic_1 = s[start:i]

            if (i+1 <= lenth and s[start:i+1] not in s_re) or i+1 > lenth:
                palindromic_2 = s_re[lenth -i: lenth-start]
                if palindromic_1 == palindromic_2:
                    curr_len = i - start
                    max_len = curr_len
                    max_str = palindromic_1
                else:
                    start = start + 1
                    i = start + max_len
            i = i + 1

        
        return max_str
            