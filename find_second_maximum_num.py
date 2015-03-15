# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = input()

s = sys.stdin.readline().rstrip()
s = s.split()
s = list(set(map(int, s)))
s.sort(reverse=True)
print s[1]
