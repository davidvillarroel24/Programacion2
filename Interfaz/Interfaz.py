import tkinter as tk

root = tk.Tk()
root.title("Label con Imagen")
root.geometry("300x300")

# Cargar una imagen (solo PNG o GIF)
imagen = tk.PhotoImage(file="Windows.png")


# Crear un Label con imagen
label_imagen = tk.Label(root, image=imagen)
label_imagen.pack()

root.mainloop()
