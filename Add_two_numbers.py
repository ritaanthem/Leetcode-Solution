'''
this is the solution, which uses less time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m1 = l1
        m2 = l2
        while m1.next != None and m2.next != None:
            m1.val += m2.val
            if m1.val >= 10:
                m1.val -= 10
                if m1.next == None:
                    m1.next = ListNode(1)
                else:
                    m1.next.val += 1
            m1 = m1.next
            m2 = m2.next
        m1.val += m2.val
        if m1.next == None:
            m1.next = m2.next
        while m1 != None:
            if m1.val >= 10:
                m1.val -= 10
                if m1.next == None:
                    m1.next = ListNode(1)
                else:
                    m1.next.val += 1
            m1 = m1.next
        return l1

'''

'''
This is my solution, using less memory, using the simple sum-carry method
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        isnone = False
        curr_node = ListNode()
        result = curr_node
        more_add = 0
        count = 0
        while l1 and l2:
            curr_node.val = (l1.val + l2.val + more_add) % 10
            more_add = (l1.val + l2.val + more_add) // 10
            if l1.next or l2.next or more_add != 0:
                next_node = ListNode(more_add)
                curr_node.next = next_node
                curr_node = curr_node.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            l1 = l2

        while l1:
            curr_node.val = (l1.val + more_add) % 10
            more_add = (l1.val + more_add) // 10
            if l1.next or more_add != 0:
                next_node = ListNode(more_add)
                curr_node.next = next_node
                curr_node = curr_node.next
            l1 = l1.next
        return result

