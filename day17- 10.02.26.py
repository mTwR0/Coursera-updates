# regex
# repetition qualifiers: {2,10} --> de cate ori se repeta patternul din fata --> range intre 2 si 10
#                       daca ai avea {2,} --> minim 2 max cat o fi
#                       la fel, {,4} e de la 0 la 4
#   \b --> word limit at beginning or end of patttern
#   print(re.findall(r'\b[\w]{2}\b','a b c d e ff')) --> iese doar ff gasit

import re   

# print(re.findall(r'\b[\w]{2}\b','a b c d e ff'))
text = 'some baaad stuff occured in this pc. the process id [12345] caused an error'
# result =(re.search(r'\[\d*\]',text))
# print(result[0])

def extract_ID(text):
    regex= r'\[\d+\]'
    result = re.search(regex,text)
    if result== None:
        return "did not find anyfin"
    return f"found somefin: {result[0]}"

print(extract_ID(text))