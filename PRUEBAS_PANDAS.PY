import openpyxl
from openpyxl.formula.translate import Translator

# Abre el archivo Excel existente
archivo_excel = 'PARTE_4.xlsx'
wb = openpyxl.load_workbook(archivo_excel)

# Selecciona la hoja en la que deseas agregar la fórmula (puedes cambiar el nombre de la hoja según tus necesidades)
hoja = wb['Sheet1']

# Agrega la fórmula a la columna 'E' a partir de la segunda fila
for fila in range(2, hoja.max_row + 1):
    celda_formula = f'E{fila}'
    celda_resultado = f'F{fila}'  # Cambia 'F' por la columna donde desees mostrar los resultados
    formula = f'CONCAT(A{fila}, C{fila}, D{fila})'

    # Traduce la fórmula antes de establecerla en la celda
    formula_traducida = Translator().translate(formula, hoja)

    # Establece la fórmula directamente en la celda
    hoja[celda_formula].value = formula_traducida

# Guarda los cambios en el archivo Excel
wb.save('nuevo_archivo.xlsx')
