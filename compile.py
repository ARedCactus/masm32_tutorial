import os, sys

def extractPathComponents(path: str) ->list:
    components = []
    path = os.path.normpath(path)
    while True:
        path, folder = os.path.split(path)
        if folder:
            components.append(folder)
        else:
            if path:
                components.append(os.path.basename(os.path.abspath(".")))
            break
    components.reverse() # 翻转
    if "." in components[-1]:
        components[-1], extension = os.path.splitext(components[-1])
        if len(extension) != 0:
            return [components, extension]
    return [components]

os.environ["INCLUDE"] = "D:\\masm32\\include"
os.environ["LIB"] = "D:\\masm32\\lib"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("参数数量错误")
        sys.exit()
    components = extractPathComponents(sys.argv[1])

    folders = ["/".join(components[0]), "build/" + "/".join(components[0][:-1]), "bin/" + "/".join(components[0][:-1])]
    for folder in folders[1:]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    print("\033[1;36m", "*.obj_path: ", "\033[0m", folders[1])
    print("\033[1;36m", "*.exe_path: ", "\033[0m", folders[2])

    command = "ml /c /coff /Fo " + folders[1]+"/"+components[0][-1]+".obj " + folders[0]+components[1] if len(components)==2 else ""
    print("\033[1;33m", command, "\033[0m")
    source_file = components[0][-1] + components[1] if len(components)==2 else ""
    obj_file = components[0][-1] + ".obj"
    command_result = source_file + " --> " + obj_file
    if not os.system(command):
        print("\033[1;32m" + command_result + "\033[0m")
    else:
        print("\033[1;31m" + command_result + " failed" + "\033[0m")
        sys.exit()
    
    exe_file = components[0][-1] + ".exe"
    command = "link /subsystem:console " + folders[1]+"/"+obj_file + " /out:"+folders[2]+"/"+exe_file
    print("\033[1;33m", command, "\033[0m")
    command_result = obj_file + " --> " + exe_file
    if not os.system(command):
        print("\033[1;32m" + command_result + "\033[0m")
    else:
        print("\033[1;31m" + command_result + " failed" + "\033[0m")



