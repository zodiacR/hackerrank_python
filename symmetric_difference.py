# Enter your code here. Read input from STDIN. Print output to STDOUT
n,list1,m,list2 = raw_input(), raw_input(),raw_input(),raw_input()

list1 = set(map(int,list1.split()))
list2 = set(map(int,list2.split()))

sem1 = list1.difference(list2)
sem2 = list2.difference(list1)

final = list(sem1.union(sem2))
final = sorted(final)

for i in final:
    print i
