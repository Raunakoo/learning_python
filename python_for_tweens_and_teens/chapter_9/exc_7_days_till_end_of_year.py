date = int(input("what is the date today? "))
month = int(input("what month is it(say integer date form)? "))

days_passed = (month - 1) * 30 + date 

days_left = 365 - days_passed

print("number of days left till end of year", days_left)