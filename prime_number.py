def check_prime(a):
   for i in range(2, a):
      if a % i == 0:
         return False
   return True

def find_next_prime(n):
   # Not sure if you want this line or not
   if check_prime(n):
       return 0

   high = n + 1
   while True:
      
      if check_prime(high):
         return high - n
      else:
         
         high += 1

check_prime(9)
print(find_next_prime(9))