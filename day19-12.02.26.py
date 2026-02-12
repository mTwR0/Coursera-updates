# lookahead - ?=some
# 
# import re

# result = (re.findall(r'([\w]*) (?=some)','i am testing some stuff, hmm some stuff, hoh some goooood stuff'))
# print(result)

import re
def transform_record(record):
  new_record = re.sub(pattern = r'([\d]{3})\-([\d]{3})\-([\d]{4})',
  repl= r'_\1',
  string=record
  )
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator