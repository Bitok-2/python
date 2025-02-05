#Program to check whether is a leap year or not
year = 2024
if (year % 400 == 0 )and (year % 100 == 0) :
    print(year, "is a leap year".format(year) )
elif (year % 4 == 0) and (year % 100 != 0):
    print(year," is a leap year ".format(year))

else :
    print(year ,"not a leap year".format(year))


#Program to check whether letter is a vowel or consonant
x = "b"
vowels = "a","e","i","o","u"
if (x == "a" or x== "e" or x == "i" or x == "o" or x == "u"):
    print(vowels)
