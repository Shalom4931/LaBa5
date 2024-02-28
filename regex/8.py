import re

txt = input()
upper = txt.upper()
x = re.sub('[a-z]', lambda match: upper[match.start()] + " ", txt)

print(x)