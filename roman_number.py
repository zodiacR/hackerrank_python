"""
Problem Statement
You are given a Roman Number and you have to validate whether its a valid number or not. If it is valid, print True or print False. Develop a regular expression for a valid Roman number.

Input Format
A string containing Roman Characters

Output Format
A one line string containing True or False

Constraints
The number will be between 1 and 3999 (both included)

Sample Input
CDXXI

Sample Output
True
"""
import re

regex = r"^M{0,3}(CD|CM|D?C{0,3})(XL|XC|L?X{0,3})(IX|IV|V?I{0,3})$"
p = re.compile(regex)

s = raw_input()

if p.match(s):
    print "True"
else: print "False"
