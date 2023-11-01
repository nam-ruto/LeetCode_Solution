# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicates(self, head):
		if not head:
			return head
		tmp = head
		pre = head
		marked = head.val
		head = head.next
		while head:
			if(marked == head.val):
				pre.next = head.next
			else:
				marked = head.val
				pre = head
			head = head.next
		return tmp