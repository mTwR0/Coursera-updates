import re
def multi_vowel_words(text):
  pattern = r'([\w]*) (?=[(a-u){3,}]*)'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']
print(multi_vowel_words("abc a aei")) 

# my nemesis:
# returns all words with 3 or more consecutive vowels (a, e, i, o, u).
