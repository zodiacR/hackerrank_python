"""
Problem Statement
You are given N mobile numbers. Sort them in ascending order after
which print them in standard format:
    +91 xxxxx xxxxx
The given mobile numbers may have +91 or 91 or 0 written before the
actual 10 digit number. Alternatively, there maynot be any prefix at
all. 

Input Format:
An integer N followed by N mobile numbers.

Output Format:
N mobile numbers printed in different lines in the required format.

Sample Input:
3
07895462130
919875641230
9195969878

Sample Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""

def standardize(func):
    def format(num):
        return sorted([func(i) for i in num])
    return format

@standardize
def format(s):
    length = len(s)
    if length == 10:
        return "+91 %s %s" % (s[:5], s[5:])
    elif length == 11:
        return "+91 %s %s" % (s[1:6], s[6:])
    elif length == 12:
        return "+%s %s %s" % (s[:2], s[2:7], s[7:])
    else:
        return "%s %s %s" % (s[:3], s[3:8], s[8:])

n = input()

num_list = [raw_input() for i in range(n)]
fmt_list = format(num_list)

for ph in fmt_list:
    print ph
