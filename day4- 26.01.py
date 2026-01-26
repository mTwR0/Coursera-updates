# r+ read write, a append
# os.path --> things related to file infomration

# with open ("day 4 notes - 26.01.26","w") as f:
#     f.write("did:")

# with open ("day 4 notes - 26.01.26") as f:
#     print(f.readlines())

import os
if os.path.exists("day 4 notes - 26.01.26.txt"):
    print("all g")
    with open ("day 4 notes - 26.01.26.txt",'a') as f:
        f.write("why: i will use files a lot, for example txts for logs and automated testing, for example for testing AI outputs" \
        "question: i still dont understand too deeply how relative paths work - imo its useful but you need to know how to actualyl navigate between files -> go 1 directory above/ below, etc")

else:
    with open ("day 4 notes - 26.01.26.txt",'w') as f:
        f.write("did: learned about paths, wrote content to this file using the built in python file management function ")
#os.remove("day 4 notes - 26.01.26")

