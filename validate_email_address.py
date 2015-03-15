import re

p = re.compile(r"^[a-zA-Z0-9\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")

def Detect(s):
    if p.search(s):
        return s
    
n = input()
mail_list = [raw_input() for i in range(n)]

mail_list = filter(Detect, mail_list)
mail_list.sort()
print mail_list
