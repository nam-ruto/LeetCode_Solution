# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1, list2):
		head = ListNode()
		res = head
		while((list1 is not None) and (list2 is not None)):
			if(list1.val <= list2.val):
				res.next = list1
				res = res.next
				list1 = list1.next
			else:
				res.next = list2
				res = res.next
				list2 = list2.next
		while(list1 is not None):
			res.next = list1
			res = res.next
			list1 = list1.next
		while(list2 is not None):
			res.next = list2
			res = res.next
			list2 = list2.next
		res = head.next
		return res