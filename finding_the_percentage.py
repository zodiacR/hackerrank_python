# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = input()
stu = {}

while n > 0:
    s = sys.stdin.readline()
    s = s.split()
    scores = [float(i) for i in s[1:]]
    avg = sum(scores) / len(scores)
    stu[s[0]] = avg
    n -= 1
name = raw_input()
print ("%.2f") % stu[name]
