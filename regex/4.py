import re 
txt = input()

x = re.search(r'\b[A-Z]{2,}[a-z]{2,}\b', txt )

if x :
    print ("Yes")
else:
    print ("No")