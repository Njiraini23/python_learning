num1, num2 = input("Enter 2 numbers: ").split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
diff = num1 - num2
product = num1 * num2 
division = num1 / num2
rem = num1 % num2
power = num1 ** num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, division))
print("{} % {} = {}".format(num1, num2, rem))
print("{} ** {} = {}".format(num1, num2, power))
 


