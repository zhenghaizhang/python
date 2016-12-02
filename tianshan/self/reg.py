import re

bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())
