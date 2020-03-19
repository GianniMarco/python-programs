x = [1,2,3,4,5,6,"sette"]
num = 0

for i in x:
	try:
		x[num] = x[num+1]
		num += 1
	except:
		break

print(x)
