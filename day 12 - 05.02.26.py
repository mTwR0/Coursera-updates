# regex:
#       . = any chr - p.thon
#       ^python = cuvintele care incep cu python --> python, python_programmer
#       python$    = cuvintele care se termina cu python --> python, programming_python  
#       ^, $ cauta intr-o linie, nu cauta cuvintele specific. daca la finalul/ inc liniei se gasesc astea, atunci le retureezaz
#
import re
# log = "Ju ly 31 07 :51:48 my computer bad_process[12345]: ERROR Performing package upgrade"
# regex = r".."
# result = re.search(regex, log)
# print(result[1])

print( re.search(r"asa", "casa"))