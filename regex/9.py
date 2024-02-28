import re

txt = input()
x = re.sub(r'(?<!^)(?=[A-Z])' , " " , txt)

print (x)