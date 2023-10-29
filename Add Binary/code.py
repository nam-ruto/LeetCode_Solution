def sumBin(a, b, tmp):
	if(tmp == 0):
		if((a == "1" and b == "0") or (a == "0" and b == "1")):
			return 1
		elif(a == "0" and b == "0"):
			return 0
		elif(a == "1" and b == "1"):
			return -1
	elif(tmp == 1):
		if((a == "1" and b == "0") or (a == "0" and b == "1")):
			return -1
		elif(a == "0" and b == "0"):
			return 1
		elif(a == "1" and b == "1"):
			return -2


class Solution:
	def addBinary(self, a: str, b: str) -> str:
		tmp = 0
		n = max(len(a), len(b))

		# Add leading zero
		dif = len(a) - len(b)
		if(dif > 0):
			b = abs(dif)*"0" + b
		else:
			a = abs(dif)*"0" + a
			
		res = ""
		for i in range(n-1, -1, -1):
			k = sumBin(a[i], b[i], tmp)
			if(k == 1 or k == 0):
				res = str(k) + res
				tmp = 0
			elif(k == -1):
				res = "0" + res
				tmp = 1
			else:
				res = "1" + res
				tmp = 1
		if((k == -1 and res[0] == "0") or (k == -2 and res[0] == "1")):
			res = "1" + res
		return res