# spent most of my time on a test
# git init
# git add .
# git commit -m "mesaj"
# git branch -M master
# git push -u origin master
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


# with open ("csv_file.txt", 'w') as f:
#     f.write("radu,076623423,gamer god")

import csv

# f= open("csv_file.txt")
# contents= csv.reader(f)
# for row in contents:
#     name,phone,role = row
#     print(f"name is {name} phone is {phone} role is {role}")

# f.close()

accounts = [["RADULIVIU12","asda12314sazx"],["radur1235","imndoufntak123/!@."]]

# with open ("new_csv_file.csv", "w") as csv_f:
#     csv_writer = csv.writer(csv_f,lineterminator="\n")
#     csv_writer.writerows(accounts)

# with open ("new_csv_file.csv" ) as csv_f:
#     reader= csv.reader(csv_f)
#     for row in reader:
#         print(row)

accounts_keys=["username","password"]
accounts2 =[{"username":"RADULIVIU12","password":"asda12314sazx"},{"username":"radur1235","password":"imndoufntak123/!@."}]

with open ("new_csv_file.csv", "w") as csv_f:

    csv_writer = csv.DictWriter(csv_f,fieldnames=accounts_keys,lineterminator="\n")
    csv_writer.writeheader()
    csv_writer.writerows(accounts2)

with open ("new_csv_file.csv", "r") as csv_f:
    reader=csv.DictReader(csv_f)
    
    for row in reader:
        print(f"name is {row["username"]}")
        print(f"password is {row["password"]}")