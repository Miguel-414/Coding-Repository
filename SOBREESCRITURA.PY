import openpyxl

# Abre el archivo Excel existente
archivo_excel = 'PARTE_5.xlsx'
wb = openpyxl.load_workbook(archivo_excel)

# Selecciona la hoja en la que deseas agregar la fórmula (puedes cambiar el nombre de la hoja según tus necesidades)
hoja = wb['Sheet1']

# Agrega la fórmula a la columna 'E' a partir de la segunda fila
for fila in range(2, hoja.max_row + 1):
    celda_formula = f'E{fila}'
    resultado_formula = f'CONCAT(A{fila}, C{fila}, D{fila})'

    # Establece el resultado de la fórmula directamente en la celda
    hoja[celda_formula].value = resultado_formula

    # Borra las referencias a las celdas de origen
    hoja[f'A{fila}'].value = None
    hoja[f'C{fila}'].value = None
    hoja[f'D{fila}'].value = None

# Guarda los cambios en el archivo Excel
wb.save('nuevo_archivo.xlsx')
