class Solution:
	def isPalindrome(self, x):
		if(x < 0):
			return False
		tmp = x
		palin = 0
		while(tmp != 0):
			palin = (palin * 10) + (tmp % 10)
			tmp = tmp // 10
		if(palin == x):
			return True
		return False