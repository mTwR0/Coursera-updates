# import subprocess
#   --> system command as part of a pythn script --> ping de ex
#   --> subprocess.run(['system_function','system_function_parameter1'])
#       --> subprocess.run(['ipconfig','/all'])
# daca dai capture_output=True, iti tine rezultatul in stdout --> result.stdout

import subprocess
result=subprocess.run(['ipconfig','/all'],capture_output=True)
print(result.returncode) # 0 --> good
#print(result.stdout) # --> are b'...' la inceput si se vad caractere speciale /n 
                     # --> e un array de bytes. trebuie sa ii dam decode
print(result.stdout.decode()) # rezultatul e o lista 
# erorile sunt tinute in stderr
print('`'*10)
err_res = subprocess.run(["rm",'a'],capture_output=True)
subprocess.run(['sleep','2'])

# nu merge, voiam sa vad daca imi da eroare python sau daca imi da print la eroarea in sine
print(err_res.stderr)