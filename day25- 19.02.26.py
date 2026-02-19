import subprocess
#subprocess.run(["echo","hello"],capture_output=True)

# utf-8 --> most used encoding
#                               --> which array of bytes represents which character


#result = subprocess.run(['host','8.8.8.8'],capture_output=True)
#print(result.returncode)
# to change env --> copy parent env, make changes, pass this to child 


# import os
# import subprocess

# my_env = os.environ.copy()    # copiem env vechi
# my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]]) # updatam path, folosim env nou

# result = subprocess.run(["myapp"], env=my_env) # rulam cu env nou

# ~~~~~~~~~~ folosesti subprocesses doar cand e absolut necesar, ca se strica grav daca il muti de pe un sistem pe altu
# linux vs windows for ex

# Subprocess: 

# subprocess.run(['mkdir', 'test_dir_subprocess2'])

# OS: 

# os.mkdir('test_dir_os2')

# Pathlib: 

# test_dir_pathlib2 = Path('test_dir_pathlib2')