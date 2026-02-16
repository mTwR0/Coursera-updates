import re
def parse_city_state(text):
 pattern = r'([\w]*[,\.]+) ([\w]+)' #enter the regex pattern here
 result = re.search(pattern, text) #enter the re method  here
 print('debugging:',result)
 if len(result) != 2: # this causes an error - i do not know how to check the len of a search obj
  return ""
 return result[2] #return the correct capturing group


print(parse_city_state("Hamilton, MN")) # should return MN
print(parse_city_state("Albuquerque, New Mexico")) # should return New Mexico
print(parse_city_state("Portland. Oregon")) # should return Oregon