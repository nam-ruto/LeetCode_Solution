class Solution:
	def longestCommonPrefix(self, strs):
		n = len(strs)
		minStr = len(min(strs, key=len))
		res = ""
		for i in range(0, minStr):
			identityChar = strs[0][i]
			count = 0
			for j in range(0, n):
				if(strs[j][i] == identityChar):
					count += 1
					if count == n:
						res += identityChar
				else:
					return res
		return res