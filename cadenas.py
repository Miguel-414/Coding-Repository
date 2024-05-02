# def merge_the_tools(string, k):
#     division = [string[i:i+k] for i in range(0, len(string), k)]
#     for parte in division:
#         parte_sin_duplicados = ''
#         for caracter in parte:
#             if caracter not in parte_sin_duplicados:
#                 parte_sin_duplicados += caracter
#         print(parte_sin_duplicados)

# if __name__ == '__main__':
#     string = input("Ingrese la cadena: ")
#     k = int(input("Ingrese la longitud de las partes: "))
#     merge_the_tools(string, k)

# a = int(input())
# A = set(map(int, input().split()))
# N = int(input())

# for i in range(N):
#     operation, _ = input().split()
#     new_elements = set(map(int, input().split())) 

#     perform = f'A.{operation}({new_elements})'
#     eval(perform)

# print(sum(A))

# cadena = set(map(float, input().split("/")))
# print(cadena)
from typing import Any
a: Any = 5
print(a)
a = 'hellow world'