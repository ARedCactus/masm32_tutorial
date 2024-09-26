# python 编译 masm32 脚本
## **terminal**
```bash
python compile.py <file.asm>
```
## **example**
```bash
python compile.py start\hello.asm
```
## **result**
-  *.obj_path:   build/start
-  *.exe_path:   bin/start
-  ml /c /coff /Fo build/start/hello.obj start/hello.asm
- Microsoft (R) Macro Assembler Version 6.14.8444
- Copyright (C) Microsoft Corp 1981-1997.  All rights reserved.
- 
-  Assembling: start/hello.asm
- hello.asm --> hello.obj
-  link /subsystem:console build/start/hello.obj /out:bin/start/hello.exe
- Microsoft (R) Incremental Linker Version 5.12.8078
- Copyright (C) Microsoft Corp 1992-1998. All rights reserved.
- 
- hello.obj --> hello.exe