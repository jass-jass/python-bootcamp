inp = input("Enter the numbers to be added separated by spaces :  ")
operands = inp.split(' ')
sum = 0.0
for i in operands:
	sum += int(i)
	print (i + ' + ', end='')
print (' = %.3f' %sum)
