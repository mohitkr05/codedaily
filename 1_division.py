#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
n = []
start = 2000
end = 3200
for x in range (start,end):
	if (x % 7 == 0) and (x % 5 != 0):
		n.append(str(x))
print (n)