#!/usr/bin/python
#-*-encoding: utf-8 -*-
"""
Problem Statement
Lets use decorators for building a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. You have to print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people having the same age, the printing should be done in the order of their input. For Henry Davids, the output should be
Mr. Henry Davids
For Mary George, the output should be
Ms. Mary George

Input Format
The first lines contain integer N followed by N lines. Each line contains firstname, lastname, age and sex separated by a single space character.
Constraints 
1<=N<=10

Output Format
N names printed in N different lines.

Sample Input
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""
import sys
from operator import itemgetter
n = input()
persons = [sys.stdin.readline().strip().split() for i in range (n)]
persons.sort(key=itemgetter(2))

for p in persons:
    if p[3] == "M":
        print "Mr. %s %s" % (p[0], p[1])
    else:
        print "Ms. %s %s" % (p[0], p[1])

