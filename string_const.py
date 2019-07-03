s = "abab"
count = 0

orig = ""
for i in s:
    if i not in orig:
        orig += i
        count += 1

print(count)
