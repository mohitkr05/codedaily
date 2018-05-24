#Question 2
#Level 1
#Factorial
#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#suppose the following input is supplied to the program:
#8 
#Then, the output should be:
#40320

def fact(n):
	if (n == 0 ):
		return 1
	else:
		return (n * fact(n-1))

print ("Please enter the number")
n = int(input())
print (fact(n))