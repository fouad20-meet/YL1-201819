count = 0;
num = int(input())
for i in range(1,num-1):
	if num%i==0:
		count += 1
if(count==1):
	print("prime")
else:
	print("not prime")
