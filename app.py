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
    if texto == 0 or texto == "":
        inputCounter.config(fg="red")
        submitButton.config(text="Reintentar", command=counter_pomodoros)
    elif isinstance(texto, str): 
        inputCounter.config(fg="red")
        submitButton.config(text="Reintentar", command=counter_pomodoros)
    else:
        textCounter.config(text="El numero de pomodoros elegidos son: " + texto)
        submitButton.destroy()
        inputCounter.destroy()

submitButton = tk.Button(root, text="Enviar", command=counter_pomodoros)
submitButton.pack()

# init timer
def run_timer():

    root.iconify()

    timerWindow = tk.Toplevel(root)
    timerWindow.title("Pomodoro")
    timerWindow.geometry("200x200+1150+0")

    label = tk.Label(timerWindow, text="¡Soy una cuenta regresiva!")
    label.pack(pady=20)

initLabel = tk.Label(root, text="¿Quieres comenzar?")
initLabel.pack()
initButton = tk.Button(root, text="Iniciar", command=run_timer)
initButton.pack()


root.mainloop()