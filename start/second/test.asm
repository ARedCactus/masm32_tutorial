.386  ;指令模式
.model flat,stdcall  ;平坦模式，调用规则
option casemap:none

include masm32.inc
include kernel32.inc
includelib masm32.lib
includelib kernel32.lib

;数据段
.data
    len   equ  6
.data?
    szText dw ?

.code
main PROC
    invoke StdIn, offset szText,len
    invoke StdOut, offset szText
    invoke ExitProcess,0
main   ENDP

END   main
