# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
fi = []
add = lambda a, b: a+b
power = lambda i: i**3

for i in range(n):
    if i == 0:
        fi.append(0)
    elif i == 1:
        fi.append(1)
    else:
        fi.append(add(fi[i-1], fi[i-2]))

cube = map(power, fi)
print cube
