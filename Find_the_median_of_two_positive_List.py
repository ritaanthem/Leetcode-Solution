'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

my solution 
time is O(log (m+n))
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        left = (m + n + 1) // 2
        right = (m + n + 2) // 2

        return (self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, left) + self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, right)) * 0.5


    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):

        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        if (len1> len2):
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)

        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        

        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j+1, end2, k - (j- start2 + 1))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i- start1 + 1))





            




