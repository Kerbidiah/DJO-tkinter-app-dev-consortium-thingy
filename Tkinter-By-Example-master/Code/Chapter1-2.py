import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        #basically everything is the same, but we use self instead of root
        self.label = tk.Label(self, text="hello world",
                                padx=5, pady=5)
        self.label.pack()

if __name__ == "__main__":
    root = Root()   # makes the variable "root" hold all the code for the UI, basiclly the same as root = tk.Tk()
    root.mainloop() # displays the window

"""import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="Hello World", padx=5, pady=5)

        self.label.pack()

if __name__ == "__main__":
    root = Root()
    root.mainloop()
"""