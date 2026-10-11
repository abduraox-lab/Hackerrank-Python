# Problem No 2: Given an integer n, perform the following conditional actions:
# if n is odd, print "Weird"
# if n is even and in the inclusive range of 2 to 5, print "Not Weird"
# if n is even and in the inclusive range of 6 to 20, print "Weird"
# if n is even and greater than 20, print "Not Weird"


# soluction code below:
n = int(input())
if(n%2 != 0):
    print("Weird")
else:
    if(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")

# Explanation of soluction and code:
# The code takes an integer input `n` from the user and checks its value against a series of conditions to determine what message to print.
# If n is odd, it prints "Weird".
# If n is even and in the range [2, 5], it prints "Not Weird".
# If n is even and in the range [6, 20], it prints "Weird".
# If n is even and greater than 20, it prints "Not Weird".
