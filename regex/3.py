import re 
txt = input()

x = re.search(r'\b[a-z]+(?:_[a-z]+)+\b', txt )

if x :
    print ("Yes")
else:
    print ("No")