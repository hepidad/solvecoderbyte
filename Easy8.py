#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Check%20Nums&lan=Python
'''
Using the Python language, have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.  
Input = 3 & num2 = 122Output = "true"
Input = 67 & num2 = 67Output = "-1" 
'''

def CheckNums(num1, num2):
	if num1 < num2:
		print "true"
	elif num1 > num2:
		print "false"
	else: print "-1"

num1 = raw_input('Input num1:')
num2 = raw_input('Input num2:')

CheckNums(num1, num2)
