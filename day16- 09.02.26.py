#   capturing groups
# \w pare mai degraba sa inlocuiasca un caracter sincer. nu e de la word cum credeam:
# r'^(\w), (\w)$' imi da  match='u, g'> dar r'^(\w*), (\w*)$' imi da match='uuuu, gggg'> adica totce cautam
import re

pattern= r'^([\w\s \.-]*), ([\w\s \.-]*)$'

print(re.search(pattern,'radu, gherman z.'))
# result = re.search(pattern,'radu, gherman')
# print(result[0])
# print(result[1])
# print(result[2])

# def rearrange_name(name):
#     pattern= r'^([\w\s .-]*), ([. -\w\s]*)$'
#     result= re.search(pattern,name)
#     if result is not None:
#         return f'{result[2]} {result[1]} is going crazy style.'
#     else:
#         return name

#print(rearrange_name('ligma, ball Z.'))
