import tkinter as tk

root = tk.Tk()  # makes the window

# first arg is always what the object will be inside of
label = tk.Label(root,
				text="hello world",
				padx=10, pady=10)

label.pack() # actually puts in into the root
			 # also grid() could do it, but differently

root.mainloop()  # shows the window

"""
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World", padx=10, pady=10)
label.pack()

root.mainloop()
"""
