
string = "monkey love banana"

s = string.split()[::-1]

l = []

for i in s:
    l.append(i)

print(" ".join(l))