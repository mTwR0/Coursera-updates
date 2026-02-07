# more regex
#           + --> orice numar de caracterul dinainte e mathcuit: print(re.search(r'a+b+','abbbbbbc'))
#           ? --> optional:  print(re.search(r'l?eague','eague'))
#           ca sa matchuiesti caractere speciale -> . , [] / etc, pui \: print(re.search(r'\.','i love dots.'))
#           \w --> any word character --> print( re.search(r'\w*','many many words'))
#           \d digits \s whitespace 
#       
#

import re

# print(re.search(r'a+b+','abbbbbbc'))
# print(re.search(r'l?eague','eague'))
# print(re.search(r'\.','i love dots.'))
# print( re.search(r'\w*','many many words'))

pattern= r'^[a-zA-Z_][\w\d_]*$'

print(re.search(pattern,'variable_name'))
print(re.search(pattern,'_variable_name_'))
print(re.search(pattern,'_variable_name'))
print(re.search(pattern,'variable_name_'))
print(re.search(pattern,' _variable_name_'))
print(re.search(pattern,'_variable name_'))
print(re.search(pattern,'1_variable_name'))

# This line of code matches any positive or negative number, with or without decimal places.
# -21.321
pattern = r'^-?\d*(.\d)+$'
print(re.search(pattern,'-21.31231'))
print(re.search(pattern,'31231'))
print(re.search(pattern,'-21. 1231'))

