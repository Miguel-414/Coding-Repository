import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_name():
    name = entry.get().strip()  # Eliminar espacios en blanco al inicio y al final
    if name:  # Verificar si se ingresó un nombre
        try:
            c.execute("INSERT INTO names VALUES (?)", (name,))
            conn.commit()
            entry.delete(0, tk.END)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo agregar el nombre: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")

def show_names():
    try:
        c.execute("SELECT * FROM names")
        names = c.fetchall()
        if names:
            message = '\n'.join(name[0] for name in names)
            messagebox.showinfo('Nombres', message)
        else:
            messagebox.showinfo('Nombres', 'No hay nombres en la base de datos.')
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"No se pudieron recuperar los nombres: {e}")

# Conexión a la base de datos
conn = sqlite3.connect('names.db')
c = conn.cursor()

# Creación de la tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS names (name TEXT)''')

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Nombres")

# Crear etiqueta y cuadro de texto para el nombre
label = tk.Label(root, text='Ingrese un nombre:')
label.pack()
entry = tk.Entry(root)
entry.pack()

# Crear botón para agregar el nombre a la base de datos
add_button = tk.Button(root, text='Agregar Nombre', command=add_name)
add_button.pack()

# Crear botón para mostrar todos los nombres en la base de datos
show_button = tk.Button(root, text='Mostrar Nombres', command=show_names)
show_button.pack()

# Ejecutar el bucle de eventos de Tkinter
root.mainloop()

# Cerrar la conexión a la base de datos al 
