#A python program that checks for room temperature

temperature = 23
if temperature > 25 :
    print("it is too hot")
else :
    print("it is too cold")

#A program that returns the largest number
first = 92
second = 40
third = 54

if first > second and first > third :
    print(first, "is the largest number")
elif second > first and second > third :
    print(second, "is the largest number")
else :
    print(third, "is the largest number")
#Program to check a number and return whether the number is even or not
#A number is even if divided the remainder is 0
#A number is odd if divided the remainder is 1

number =0
if number == 0 :
    print(number, "is a neutral number ")

num = int(input("Enter a number :"))
if (num % 2) == 0 :
    print("num is even".format(num))
else :
    print("num is odd ".format(num))

