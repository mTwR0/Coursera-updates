# os.path --> getmtime = last modified time --> unix
#          --> abspath = absolute path of a file
#          --> .join dintre C:\Users\gherm\Desktop\study\coursera si day 5 notes ... doar adauga un \, dar face altcv pe alt OS!!!
# datetime --> datetime.datetime.fromtimestamp --> get actual date


import os

# with open ("day 5 notes - 27.01.26.txt","w") as f:
#     f.write("did: ")
print(os.path.abspath("day 5 notes - 27.01.26.txt"))
print(os.getcwd())
print(os.listdir(os.getcwd()))

# git init
# git add .
# git commit -m "mesaj"
# git branch -M main
# git push -u origin main
# with open ("day 1 notes- 23.01.26.txt") as f:
#     print( f.readlines())