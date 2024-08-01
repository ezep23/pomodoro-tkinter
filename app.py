from PIL import Image, ImageTk

try:
    import Tkinter as tk  #Python 2.0
except ImportError:
    import tkinter as tk  #Python 3.0


root = tk.Tk()

# Icon
icon = Image.open('./img/icon.png')  
icon_tk = ImageTk.PhotoImage(icon)

root.geometry("300x300+500+200")
root.resizable(False,False)
root.iconphoto(True, icon_tk)
root.title("Pomodoro")


# Content root
label = tk.Label(root, text="¡Bienvenido a la aplicación! ")
label.pack(pady=20)

counter = tk.Frame(root)
counter.configure(width=200, height=200, bg="red")
counter.pack()



root.mainloop()