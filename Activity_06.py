inp = input("Enter 5 numbers :  ")
number = inp.split(' ')
for i in range(0, 5):
	number[i] = int(number[i])
number3 = number[0:3]
print("sliced list = ",number3)
number[0]=0
number[4]=0
number3[0]=0
number3[2]=0
print("replaced list-1 = ",number)
print("replaced list-2 = ",number3)
