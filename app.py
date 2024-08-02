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
mainText = tk.Label(root, text="¡Bienvenido a la aplicación! ")
mainText.pack(pady=20)

textCounter = tk.Label(root, text="Ingrese el numero de pomodoros a realizar: ")
textCounter.pack()
inputCounter = tk.Entry(root)
inputCounter.pack()

def counter_pomodoros():
    texto = inputCounter.get()
    textCounter.config(text="El numero de pomodoros elegidos son: " + texto)

    submitButton.destroy()
    inputCounter.destroy()

submitButton = tk.Button(root, text="Enviar", command=counter_pomodoros)
submitButton.pack()

# init timer

initLabel = tk.Label(root, text= "¿Quieres comenzar?")
initButton = tk.Button(root, text="Iniciar", command=runTimer)

def 

root.mainloop()