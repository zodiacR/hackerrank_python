"""
Problem Statement
You are given a valid XML document and you have to print its score. The first line of input is the number of XML lines followed by the XML lines. Score is given by the sum of score of each element. For any element, score is equal to the number of attributes it has.

Input Format
The first line shows the number of lines in XML document followed by the XML document.

Output Format
An integer score

Sample Input
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output
5
"""
from xml.etree import ElementTree

n = input()
s = ""

while n > 0:
    s += raw_input()
    n -= 1

tree = ElementTree.XML(s)

sum = 0

for i in tree.iter():
    sum += len(i.attrib)

print sum
