# regex stuff
# r for raw string -> nu itner[preta nimci ca un caracter special
#
# returneaza un amtch obj
#
#
#   
# <re.Match object; span=(3, 7), match='axaa'> --> span e range-ul, match = unde s-a gasit
# re.ignorecase --> ignore case
import re
# search iti da doar primul match
# findall gaseste tot wow
# print(re.search(r'axa.','AXAx axa', re.IGNORECASE))
# [] character classes --> orice pui intre ele ia match. poti sa pui si ' '. daca pui ^ e negatie
# | pipe iti da una sau alta
# * --> indicates zero or more occurrences of the preceding element

# repeated matches --> .* matches any characters repeated as many times, including 0
# match py , any numebr of any chr, ending with n 
print(re.search(r'H.*o|Goo.*e ','Hello and Goodbye'))
# --> Hello and Goo pentru ca vrea sa ia cat mai multe caractere
print(re.search(r'hello|world','THE WORLD',re.IGNORECASE))
print(re.findall(r'hello|world','hello THE WORLD',re.IGNORECASE))

print(re.search(r'[a-q ]erial',' erial'))

