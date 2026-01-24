# modules are different from just file imports , you can create them and split them - you msut create 
# an __init__.py file for python to recognize you wanted to create a module
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

import math
import psutil
import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    return (du.free/du.total)*100>20

def check_cpu_usage():
    cu= psutil.cpu_percent(3)
    return cu<50

def circle(raza):
    return math.pi*(raza**2)

def donut(raza_inside, raza_outside):
    return circle(raza_outside)- circle(raza_inside)

if not check_cpu_usage or not check_disk_usage:
    print("system not healthy")
else:
    print("all ok")