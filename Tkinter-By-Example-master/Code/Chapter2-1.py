import tkinter as tk


class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__() # have no idea what this does

		# if no tasks are supplied, create an empty list, otherwise, save it in the object
		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks

		self.title("To-Do App v1")
		self.geometry("300x400")  # user can change, but it subconsoucly signals to user to keep it tall

		# this sets up the first entry, which is a label that says add here
		todo1 = tk.Label(self, text="---add here---", bg="lightgray", fg="black", pady=10)
		self.tasks.append(todo1)

		# "packs" all the tasks that were given when inited
		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)

		# is this a text input box?
		self.taskCreate = tk.Text(self, height=3, bg="white", fg="black")

		self.taskCreate.pack(side=tk.BOTTOM, fill=tk.X)  # packs the text input?
		self.taskCreate.focus_set()  # sets typing focus to the box?
		self.bind("<Return>",
				  self.addTask)  # key binding DON'T PUT PARENTHESES AT END, we want the func itself, not the func to do its thing

		# defines the color schemes
		self.colorScheme = [{"bg": "lightgrey", "fg": "black"},
							{"bg": "grey", "fg": "white"}]

	def addTask(self, event=None):
		taskText = self.taskCreate.get(1.0,
									   tk.END).strip()  # gets text from the box and removes front and back whitespace

		if len(taskText) > 0:  # makes sure the input isn't blank
			newTask = tk.Label(self, text=taskText, pady=10)  # makes the label

			# toggles each line between gray and white
			taskStyleChoice = len(self.tasks) % 2
			mySchemeChoice = self.colorScheme[taskStyleChoice]

			# sets the bg and fg colors
			newTask.configure(bg=mySchemeChoice["bg"])
			newTask.configure(fg=mySchemeChoice["fg"])

			# packs and adds to the list of entries
			newTask.pack(side=tk.TOP, fill=tk.X)
			self.tasks.append(newTask)

		self.taskCreate.delete(1.0, tk.END)  # clears the text box


# if this program is ran (not imported) do this
print(__name__)
if __name__ == "__main__":
	Todo().mainloop()

"""
import tkinter as tk

class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__()

		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks

		self.title("To-Do App v1")
		self.geometry("300x400")

		todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)

		self.tasks.append(todo1)

		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)

		self.task_create = tk.Text(self, height=3, bg="white", fg="black")

		self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
		self.task_create.focus_set()

		self.bind("<Return>", self.add_task)

		self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

	def add_task(self, event=None):
		task_text = self.task_create.get(1.0,tk.END).strip()

		if len(task_text) > 0:
			new_task = tk.Label(self, text=task_text, pady=10)

			_, task_style_choice = divmod(len(self.tasks), 2)

			my_scheme_choice = self.colour_schemes[task_style_choice]

			new_task.configure(bg=my_scheme_choice["bg"])
			new_task.configure(fg=my_scheme_choice["fg"])

			new_task.pack(side=tk.TOP, fill=tk.X)

			self.tasks.append(new_task)

		self.task_create.delete(1.0, tk.END)

if __name__ == "__main__":
	todo = Todo()
	todo.mainloop()
"""
