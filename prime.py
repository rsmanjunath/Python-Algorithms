"""start = 11
end = 27

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               break
            else:
               print(num)
               break"""



lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))


for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)





"""num = 11

# If given number is greater than 1
if num > 1:

# Iterate from 2 to n / 2
    for i in range(2, num):

    # If num is divisible by any number between
    # 2 and n / 2, it is not prime
        if (num % i) == 0:
    	    print(num, "is not a prime number")
    	    break
        else:
            print(num, "is a prime number")
            break

else:
    print(num, "is not a prime number")"""
