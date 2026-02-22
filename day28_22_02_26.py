# renamed like this because the name with . causes errors when imported in the test script
# unit tests --> isolated tests to check specific part of code - e.g. function/ class
# aaa, bbb --> bbb aaa

import re
def rearrange_name(name: str):
    pattern = r'^([\w]+), ([\w]+)$'
    result = re.match(pattern=pattern,string=name)
    return f'{result[2]} {result[1]}'
    pass

print(rearrange_name('ligma, balls'))

# write code that runs test, verifies outptut