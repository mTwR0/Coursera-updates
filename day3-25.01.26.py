# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# git init
# git add .
# git commit -m "mesaj"
# git branch -M main
# git push -u origin main
# with open ("day 1 notes- 23.01.26.txt") as f:
#     print( f.readlines())

with open ("day 1 notes- 23.01.26.txt") as f:
    for line in f:
        print(line.strip().upper())

f = open("day 1 notes- 23.01.26.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line.upper())