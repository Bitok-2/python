# The Following code checks if the user-provided number is prime or not

# Defining the function
# Logic : A number is not prime if :
# 		1. it is less than equal to 1 and
# 		2. it is divisible by any number except 1 and itself

def is_prime(number):
  if number > 1:
    for i in range(2,number):
      if (number % i) == 0:
        return False
    return True
  else:
    return False

# Taking user input
number = int(input("Enter a number to check: "))

# Condition Checking
if is_prime(number):
  print(f"{number} is a prime number.")
else:
  print(f"{number} is not a prime number.")