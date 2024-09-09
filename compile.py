import os, sys
from pathlib import Path

if len(sys.argv) != 2:
    print("At least one parameter")
    sys.exit()

def getFileName(file_path: str) ->str:
    str_tuple = os.path.splitext(os.path.basename(file_path))
    return str_tuple[0]

def getParentDir(flie_path: str) ->str:
    path = Path(path_file)
    return path.parent.name
    
path_file = str(sys.argv[1])
parent_dir = getParentDir(path_file) + "/"
path_obj = "build/" + parent_dir + getFileName(path_file) + ".obj"

dir_paths = ["build", "bin", "build/"+parent_dir, "bin/"+parent_dir]
for dir in dir_paths:
    if not os.path.exists(dir):
        os.makedirs(dir)

command = "ml /c /coff /Fo " + path_obj + " " + path_file
if(not os.system(command)):
    print("\033[1;32m" + path_file + " --> " + path_obj + "\033[0m")
else:
    print("\033[1;31m" + path_file + " --> " + path_obj + " failed\033[0m")
    sys.exit()

path_exe = "bin/" + parent_dir + getFileName(path_file) + ".exe"
command = "link /subsystem:console " + path_obj + " /out:" + path_exe
if(not os.system(command)):
    print("\033[1;32m" + path_obj + " --> " + path_exe + "\033[0m")
else:
    print("\033[1;31m" + path_obj + " --> " + path_exe + " failed\033[0m")
    sys.exit()

