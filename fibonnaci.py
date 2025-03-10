
sequence = [0,1]
runs = 10
a = sequence[0]
b = sequence[1]


for i in range(1, runs):
    c = a+b
    a = b 
    b = c
    sequence.append(c)

print(sequence)



