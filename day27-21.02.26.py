# sys.argv[0] = nume script
# sys.argv[1] = argument 1, etc
#
import re, sys
usernames= {}
# user = 'hyprusr'
# usernames[user] = usernames.get(user,0) +1
# usernames[user] = usernames.get(user,0) +1
# # usernames.get(user) returneaza valoarea cheii din dict pt user. faptul ca pui 0 dupa 
# # il face sa fie pusa ca valoare default daca nu apare deloc userul 
# print(usernames[user])

with open ('syslog.txt') as f:
    pattern = r'(CRON\[\d*\])(.*)(user [\w]* )'
    for line in f:
        if 'CRON' not in line:
           # print('next')
            continue
        #print(line.strip())
        result = re.search(pattern=pattern,string=line)
        if result is None:
            continue
        print(result[1],'||', result[3])
        usernames[result[3]] = usernames.get(result[3],0)+1

print(usernames)

test = 'IP (0212)'
print(re.findall(pattern=r'IP \(\d+\)',string=test))