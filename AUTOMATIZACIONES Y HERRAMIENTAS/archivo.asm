section .data
    msg db 'Hola, mundo!', 0

section .text
    global _start

_start:
    ; Escribir el mensaje en la salida estándar
    mov eax, 4            ; syscall para sys_write
    mov ebx, 1            ; fd (file descriptor) 1 para stdout
    mov ecx, msg          ; puntero al mensaje
    mov edx, 13           ; longitud del mensaje
    int 0x80              ; llamar al kernel

    ; Salir del programa
    mov eax, 1            ; syscall para sys_exit
    xor ebx, ebx          ; código de salida 0
    int 0x80              ; llamar al kernel
