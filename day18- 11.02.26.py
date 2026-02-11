#
# split returneaza bucatile din text pt care dai split:
#   re.split(r'[.!?]','ooga. ooga booga!')
#   daca vrei sa apara si . ! ? ca splituri, pui chestiile dupa care dai split in ()
# re.sub --> replacement
# print(re.sub(pattern=r"[\w\d-]+@[\w.-]+",string="radman@radorg.gov",repl='[replaced_email]'))
# re.sub(pattern, string, repl) repl poate sa fie un regex
# 
import re   

# print(re.findall(r'\b[\w]{2}\b','a b c d e ff'))
text = 'some baaad stuff occured in this pc. the process id [12345] caused an error'
# result =(re.search(r'\[\d*\]',text))
# print(result[0])

# pentru ca ai folosit () la ambele parti din regex, ai 2 grupuri, deci poti sa le accesezi cu [1] si [2]
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return f'{result[1]} ({result[2]})'


#print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)

print(re.split(r'[.!?]','ooga. ooga booga!')) # ['ooga', ' ooga booga', '']

print(re.sub(pattern=r"[\w\d-]+@[\w.-]+",string="radman@radorg.gov",repl='[replaced_email]'))

# asta are 2 grupuri: hi, hello
# in repl ma refer la \2 ca la capture grupul 2 si la 1 ca la primul grup -->  hello hi world
print(re.sub(pattern=r'(hi), (hello)',
    string='hi, hello world',
    repl=r'\2 \1'
))