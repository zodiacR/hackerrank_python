# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
s = sys.stdin.readline()
sub = sys.stdin.readline()
s = list(s)
s = zip(*[s[i:] for i in range(len(sub))])
s = ["".join(i) for i in s]
print s.count(sub)
