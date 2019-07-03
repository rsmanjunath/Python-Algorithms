n = int(input())
first_input = set(input())

for i in range(n-1):
    rest_input = set(input())
    first_input = first_input & rest_input

print(len(first_input))