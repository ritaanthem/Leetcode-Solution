'''
this is solution, which the least time
Removes the previous value from the set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        i = 0
        max_len = 0
        count = 0
        su = set()
        for k in s:
            count+=1
            while k in su:
                count-=1
                su.remove(s[i])
                i+=1
            su.add(k)
            max_len = count if count>max_len else max_len
        return max_len
'''

'''
this is solution, which the least memory
count and find and remover
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter=collections.Counter()
        i=j=0
        length=len(s)
        res=0
        while j<length:
            counter[s[j]]+=1
            if counter[s[j]]>1:
                res=max(res,j-i)
                while i<j and s[i]!=s[j]:
                    counter[s[i]]-=1
                    i+=1
                if i<length:
                    counter[s[i]]-=1
                i+=1
            j+=1
        return max(res,j-i)

'''
'''
this is my solution'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = -1
        for c in s:
            if c in s[start:end]:
                curr_len = end - start
                if curr_len > max_len:
                    max_len = curr_len
                start = start + s[start:end].find(c) + 1
                end = end + 1
            else:
                end = end + 1

        curr_len = end - start
        if curr_len > max_len:
            max_len = curr_len
        return max_len
        
        
                