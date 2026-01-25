# 5 days* 15 min* 3/day * 4weeks
# 10h total time 
# relative vs absolute paths
# open - use - close

# f = open("day 1 notes- 23.01.26.txt")
# print(f.read())
# f.close()

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