# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y, z, n = input(), input(), input(), input()

xi = range(x+1)
yi = range(y+1)
zi = range(z+1)
l = [[i,j,k] for i in xi for j in yi for k in zi if i+j+k != n]
print l
