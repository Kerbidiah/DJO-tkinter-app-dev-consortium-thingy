import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__()

		# if no tasks are supplied, create an empty list, otherwise, save it in the object
		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks

		# make a canvas inside the window
		# canvases allow you to do lots of stuff, one of which is scroll
		self.tasksCanvas = tk.Canvas(self)

		# a frame is a "layout component" that allows you to group stuff together
		# basically it is an (invisible) box which makes our lives easier
		self.textFrame = tk.Frame(self)

		# text input box
		self.taskCreate = tk.Text(self.textFrame, height=3, bg="white", fg="black")

		# make a frame inside the canvas
		# this is where we will put all the task label BOIs
		self.tasksFrame = tk.Frame(self.tasksCanvas)

		# make a vertical scroll bar
		self.scrollbar = tk.Scrollbar(self.tasksCanvas, orient="vertical", commmand=self.tasksCanvas.yview)
		self.tasksCanvas.configure(yscrollcommand=self.scrollbar.set)

		self.title("To-Do App v1") # title of window (shows at top)
		self.geometry("300x400") # user can change, but it *subconsciously* signals to user to keep it tall

		# make canvas take up entire window + expand to as big as possible
		self.tasksCanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # make scroll bar on right side and fill y

		# ????
		self.canvasFrame = self.tasksCanvas.create_window((0, 0), window=self.tasksFrame, anchor="n")

		# pack a bunch of stuff
		self.taskCreate.pack(side=tk.BOTTOM, fill=tk.X)
		self.tasksFrame.pack(side=tk.BOTTOM, fill=tk.X)

		self.taskCreate.focus_set() # set focus to text input

		# this sets up the first entry + key-bind
		todo1 = tk.Label(self.tasksFrame, text="---add here---", bg="lightgray", fg="black", pady=10)
		todo1.bind("<Button-1>", self.removeTask)
		self.tasks.append(todo1)

		# "packs" all the tasks that were given when inited
		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)

		# key bindings
		# for key bindings, DON'T PUT PARENTHESES AT END, we want the func itself,...
		# not the func to execute and hand a result to the bind() function
		self.bind("<Return>", self.addTask)
		self.bind("<Configure>", self.onFrameConfigure)
		self.bind_all("<MouseWheel>", self.mouseScroll)
		self.bind_all("<Button-4>", self.mouseScroll)
		self.bind_all("<button-5>", self.mouseScroll)

		# color schemes
		self.colorScheme = [{"bg": "lightgrey", "fg": "black"},
							{"bg": "grey", "fg": "white"}]

	def addTask(self):

		# gets text from the box and removes front and back whitespace
		taskText = self.taskCreate.get(1.0, tk.END).strip()

		if len(taskText) > 0: # makes sure the input isn't blank
			# make label
			newTask = tk.Label(self.tasksFrame, text=taskText, pady=10) # makes the label
			self.setTaskColor(len(self.tasks), newTask)

			# bind, pack, add
			newTask.bind("<Button-1>", self.removeTask)
			newTask.pack(side=tk.TOP, fill=tk.X)
			self.tasks.append(newTask)

		self.taskCreate.delete(1.0, tk.END) # clears the text box

	def removeTask(self, event):
		task = event.widget

		if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
			# destroy all traces of it
			self.tasks.remove(event.widget)
			event.widget.destroy()
			self.recolorTasks()

	# redo all task colors
	def recolorTasks(self):
		for index, task in enumerate(self.tasks):
			self.setTaskColor(index, task)

	# change a specific task's color (used for recolorTasks())
	def setTaskColor(self, pos, task):
		# select the scheme
		schemeNum = pos % 2
		scheme = self.colorScheme[schemeNum]

		# set the scheme
		task.configure(bg=scheme["bg"])
		task.configure(fg=scheme["fg"])

	def onFrameConfigure(self):
		self.tasksCanvas.configure(scrollregion=self.tasksCanvas.bbox("all"))

	def taskWidth(self, event):
		canvasWidth = event.width
		self.tasksCanvas.itemconfig(self.canvasFrame, width=canvasWidth)

	# does the scrolling shenanigans
	def mouseScroll(self, event):
		# I added this line because it otherwise the program could ...
		# get to "self.tasksCanvas.yview_scroll(move, "units")" w/o ...
		# having defined what move equals
		move = 0

		if event.delta:
			self.tasksCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
		elif event.num == 5:
			move = 1
		else:
			move = -1
		self.tasksCanvas.yview_scroll(move, "units")


# if this program is ran (not imported) do this
if __name__ == "__main__":
	Todo().mainloop() # display the window

"""
import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__()

		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks

		self.tasks_canvas = tk.Canvas(self)

		self.tasks_frame = tk.Frame(self.tasks_canvas)
		self.text_frame = tk.Frame(self)

		self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

		self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

		self.title("To-Do App v2")
		self.geometry("300x400")

		self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

		self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
		self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

		self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

		self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
		self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
		self.task_create.focus_set()

		todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
		todo1.bind("<Button-1>", self.remove_task)

		self.tasks.append(todo1)

		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)

		self.bind("<Return>", self.add_task)
		self.bind("<Configure>", self.on_frame_configure)
		self.bind_all("<MouseWheel>", self.mouse_scroll)
		self.bind_all("<Button-4>", self.mouse_scroll)
		self.bind_all("<Button-5>", self.mouse_scroll)
		self.tasks_canvas.bind("<Configure>", self.task_width)

		self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

	def add_task(self, event=None):
		task_text = self.task_create.get(1.0,tk.END).strip()

		if len(task_text) > 0:
			new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

			self.set_task_colour(len(self.tasks), new_task)

			new_task.bind("<Button-1>", self.remove_task)
			new_task.pack(side=tk.TOP, fill=tk.X)

			self.tasks.append(new_task)

		self.task_create.delete(1.0, tk.END)

	def remove_task(self, event):
		task = event.widget
		if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
			self.tasks.remove(event.widget)
			event.widget.destroy()
			self.recolour_tasks()

	def recolour_tasks(self):
		for index, task in enumerate(self.tasks):
			self.set_task_colour(index, task)

	def set_task_colour(self, position, task):
		_, task_style_choice = divmod(position, 2)

		my_scheme_choice = self.colour_schemes[task_style_choice]

		task.configure(bg=my_scheme_choice["bg"])
		task.configure(fg=my_scheme_choice["fg"])

	def on_frame_configure(self, event=None):
		self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

	def task_width(self, event):
		canvas_width = event.width
		self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

	def mouse_scroll(self, event):
		if event.delta:
			self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
		else:
			if event.num == 5:
				move = 1
			else:
				move = -1

			self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
	todo = Todo()
	todo.mainloop()
"""