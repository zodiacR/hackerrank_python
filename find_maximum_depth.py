"""
Problem Statement

You are given a valid XML document and you have to print the maximum level of nesting in it. The first line of input is the number of XML lines followed by the XML lines. Take the depth of root as 0.

Input Format
The first line shows the number of lines in XML document followed by the XML document.

Output Format
An integer value

Sample Input
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output
1
"""
from xml.etree import ElementTree

n = input()
s = ""

while n > 0:
    s += raw_input()
    n -= 1

tree = ElementTree.XML(s)

def depth(p):
    return max([0] + [depth(child)+1 for child in p])


print depth(tree)
