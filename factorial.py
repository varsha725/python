# 1st Method
def factorial(n):
return 1 if (n==1 or n==0) else n * factorial(n - 1);
#Driver Code
num = 5;
print("Factorial of",num,"is",factorial(num));
#Note that using semicolon as a statement delimiter is also acceptable in Python.

# 2nd Method
def factorial(n):
if n < 0:
return 0
elif n == 0 or n == 1:
return 1
else:
fact = 1
while(n > 1):
fact *= n
n -= 1
return fact

# Driver Code
num = 5;
print("Factorial of",num,"is",factorial(num))

# 3rd Method
import math
def factorial(n):
return(math.factorial(n))
# Driver Code
num = 5
print("Factorial of", num, "is",factorial(num))
