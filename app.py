from PIL import Image, ImageTk

try:
    import Tkinter as tk  #Python 2.0
except ImportError:
    import tkinter as tk  #Python 3.0

# Icon
icon = Image.open('./img/icon.png')  

class menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.geometry("300x300+500+200")
        self.icon_tk = ImageTk.PhotoImage(icon)
        self.resizable(False,False)

        self.etiqueta = tk.Label(self, text="¡Bienvenido a la aplicación! ") 
        self.etiqueta.pack(pady=20)

        self.textoPomodoros = tk.Label(self, text="Ingrese el numero de pomodoros a realizar: ")
        self.textoPomodoros.pack()
        
        self.inputPomodoros = tk.Entry(self)
        self.inputPomodoros.pack()

        entrada = self.inputPomodoros.get()
        
        if entrada == 0 or entrada == "":
            self.inputPomodoros.config(fg="red")
            submitButton.config(text="Reintentar", command=counter_pomodoros)
        elif isinstance(texto, str): 
            self.inputPomodoros.config(fg="red")
            submitButton.config(text="Reintentar", command=counter_pomodoros)
        else:
            self.textoPomodoros.config(text="El numero de pomodoros elegidos son: " + entrada)
            submitButton.destroy()
            inputCounter.destroy()


    def cronometro_pomodoros(self):
        cronometro_pomodoros = pomodoro(self)
        cronometro_pomodoros.grab_set()

class pomodoro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pomodoro")
        self.geometry("200x200+1150+0")

if __name__ == "__main__":
    app = menu()
    app.mainloop()