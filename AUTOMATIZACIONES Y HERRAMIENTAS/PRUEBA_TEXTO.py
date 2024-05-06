# divide un archivo de excel en determinado numero de registros recuerde poner la ruta de acceso 
# al documento que desea dividir
import pandas as pd

archivo_excel = 'PRUEBA_DE_DIVISION_DE_ARCHIVOS_CANTIDAD_100.xlsx' # Lee el archivo Excel seleccionado
df = pd.read_excel(archivo_excel)
registros_por_archivo = 100 # Define el número máximo de registros por archivo
total_registros = len(df) # Calcula la cantidad de archivos que necesitarás
total_archivos = total_registros // registros_por_archivo + 1

# Divide el DataFrame en partes más pequeñas y guarda cada parte en un archivo Excel
for i in range(total_archivos):
    inicio = i * registros_por_archivo
    fin = (i + 1) * registros_por_archivo
    parte_df = df.iloc[inicio:fin]
    nombre_archivo = f'PARTE_{i + 1}.xlsx'
    parte_df.to_excel(nombre_archivo, index=False)

print(f'Se han creado {total_archivos} archivos más pequeños.')