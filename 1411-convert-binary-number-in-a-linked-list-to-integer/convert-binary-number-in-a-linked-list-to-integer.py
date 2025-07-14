# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num_arr = []
        curr = head
        while curr:
            num_arr.append(curr.val)
            curr = curr.next
        
        result = 0
        for i in range(len(num_arr) - 1, -1, -1):
            result += (2 ** (len(num_arr) - 1 - i)) * num_arr[i]

        return result
        