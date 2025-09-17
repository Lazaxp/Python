#Get the summation of every odd input
pre = 0
for x in range(10):
	a = eval(input("input numbers numbers 10 times"))
    lev = a % 2
    if lev == 1:
		pre+=a
print("The summation of odd inputs are:",pre)
    
