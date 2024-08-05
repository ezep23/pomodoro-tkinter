try:
    import Tkinter as tk  #Python 2.0
except ImportError:
    import tkinter as tk  #Python 3.0

#Icono
from PIL import Image, ImageTk

from tkinter import messagebox
from threading import Thread, Event
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        
        # Variables
        self.pomodoros = tk.IntVar(value=1)
        self.duration = tk.IntVar(value=25)
        self.timer_thread = None
        self.stop_event = Event()
        self.is_paused = False
        self.time_left = 0
        
        # Create Widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for Pomodoro settings
        settings_frame = tk.Frame(self.root)
        settings_frame.pack(padx=10, pady=10)
        
        tk.Label(settings_frame, text="Number of Pomodoros:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(settings_frame, textvariable=self.pomodoros).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(settings_frame, text="Duration (minutes):").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(settings_frame, textvariable=self.duration).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(settings_frame, text="Start", command=self.start_timer).grid(row=2, columnspan=2, pady=10)
        
    def start_timer(self):
        num_pomodoros = self.pomodoros.get()
        duration = self.duration.get() * 60
        self.stop_event.clear()
        self.is_paused = False
        self.time_left = duration
        
        self.timer_thread = Thread(target=self.run_timer, args=(num_pomodoros,))
        self.timer_thread.start()
        
    def run_timer(self, num_pomodoros):
        for _ in range(num_pomodoros):
            while self.time_left > 0 and not self.stop_event.is_set():
                if not self.is_paused:
                    minutes, seconds = divmod(self.time_left, 60)
                    time_str = f"{minutes:02}:{seconds:02}"
                    self.show_timer_popup(time_str)
                    time.sleep(1)
                    self.time_left -= 1
                else:
                    time.sleep(1)
                    
            if self.stop_event.is_set():
                break
        
        if not self.stop_event.is_set():
            messagebox.showinfo("Pomodoro Complete", "All pomodoros are completed!")
        
    def show_timer_popup(self, time_str):
        if not hasattr(self, 'popup'):
            self.popup = tk.Toplevel(self.root)
            self.popup.title("Pomodoro Timer")
            self.popup.geometry("200x100")
            
            self.time_label = tk.Label(self.popup, text=time_str, font=("Helvetica", 24))
            self.time_label.pack(pady=10)
            
            tk.Button(self.popup, text="Pause", command=self.pause_timer).pack(side=tk.LEFT, padx=5)
            tk.Button(self.popup, text="Stop", command=self.stop_timer).pack(side=tk.RIGHT, padx=5)
            
            self.popup.protocol("WM_DELETE_WINDOW", self.on_popup_close)
        else:
            self.time_label.config(text=time_str)
            
    def pause_timer(self):
        self.is_paused = not self.is_paused
        button_text = "Resume" if self.is_paused else "Pause"
        for widget in self.popup.winfo_children():
            if widget.cget("text") == button_text:
                widget.config(text="Pause" if not self.is_paused else "Resume")
        
    def stop_timer(self):
        self.stop_event.set()
        if hasattr(self, 'popup'):
            self.popup.destroy()
            del self.popup

    def on_popup_close(self):
        self.stop_timer()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
