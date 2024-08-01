import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

icon = Image.open('./img/logo.png')  
icon_tk = ImageTk.PhotoImage(icon)

root.iconphoto(True, icon_tk)

root.title("Pomodoro")
root.geometry("400x400")


label = tk.Label(root, text="¡Bienvenido a la aplicación! ")
label.pack(pady=20)


root.mainloop()