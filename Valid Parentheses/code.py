class Solution:
	def isValid(self, s):
		openBrackets = []
		pairBrackets = {"(":")", "{":"}", "[":"]"}
		for bracket in s:
			if bracket in pairBrackets:
				openBrackets.append(bracket)
			elif(len(openBrackets) == 0 or bracket != pairBrackets[openBrackets.pop()]):
				return False
		if(len(openBrackets) == 0):
			return True
		return False