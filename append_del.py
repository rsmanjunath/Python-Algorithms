s = "hackerhappy"
t = "hackerrank"
k = 9 
s_length = len(s)
t_length = len(t)

if s_length + t_length < k:
        print('Yes') 

same = 0
for s_l, t_l in zip(s, t):
    
    if s_l == t_l: 
        same += 1
    else: 
        break

extra_s = s_length - same
extra_t = t_length - same
difference = extra_s + extra_t
print(extra_s,extra_t,difference)

if difference <= k and difference % 2 == k % 2: 
    print('Yes')
else:
    print('No')

