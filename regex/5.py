import re

txt = input()

x = re.search ("a.*b" , txt)

if x:
    print("Yes")
else :
    print ("No")