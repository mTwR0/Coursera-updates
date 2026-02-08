# repeat regex patterns:
#

# * 0 to any number of times.

# + 1 to any number of times.

# {n} 'n' times.

# {n,} at-least 'n' times.

# [0-9]{1} this means 1 digit(0-9)



# matching groups --> groups = () --> r'^(\w*), (\w*)$' --> 
import re
pattern = r'^(\w*), (\w*)$'

result=re.search(pattern, 'adasdad, nsadad')
print(result.groups()) # --> ('a', 'n')
print(result[0]) # adasdad, nsadad
print(result[1]) # adasdad
print(result[2]) # nsadad