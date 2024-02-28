import re 
txt = input()

x = re.search('^a.{2}b$', txt )

if x :
    print ("Yes")
else:
    print ("No")