number = int(raw_input("Please input the number >" ))

x = range(1,10000000)

for i in x:


	if number % i == 0:
	
		print i
