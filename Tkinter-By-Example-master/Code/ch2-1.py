import tkinter as tk

class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__()

		# if no tasks are supplied, create an empty list, otherwise, save it in the object
		if not tasks:
			self.tasks = []
		else:
			self.tasks = tasks

		self.title("To-Do App v1")
		self.geometry("300x400") # user can change, but it subconsoucly singals to user to keep it tall

		# this sets up the first entry, which is a label that says add here
		todo1 = tk.Label(self, text="---add here---", bg="lightgray", fg="black", pady=10)
		self.tasks.append(todo1)

		# "packs" all the tasks that were given when inited
		for task in self.tasks:
			task.pack(side=tk.TOP, fill=tk.X)
		
		# is this a text input box?
		self.taskCreate = tk.Text(self, height=3, bg="white", fg="black")

		self.taskCreate.pack(side= tk.BOTTOM, fill=tk.X) # packs the text input?
		self.taskCreate.focus_set()	# sets typing focus to the box?
		self.bind("<Return>", self.addTask) # key binding DON'T PUT PARENTHESES AT END, we want the func itself, not the func to do its thing

		# defines the color schemes
		self.colorScheme = [{"bg": "lightgrey", "fg": "black"}, 						{"bg": "grey", "fg": "white"}]

	def addTask(self, event=None):
		taskText = self.taskCreate.get(1.0, tk.END).strip() # gets text from the box and removes front and back whitespace
		print("got here")
		if len(taskText) > 0: # makes sure the input isn't blank
			newTask = tk.Label(self, text=taskText, pady=10) # makes the label
			
			# toggles each line between gray and white
			_, taskStyleChoice = divmod(len(self.tasks), 2) #len(self.tasks) % 2
			mySchemeChoice = self.colorScheme[taskStyleChoice]

			# sets the bg and fg colors
			newTask.configure(bg=mySchemeChoice["bg"])
			newTask.configure(fg=mySchemeChoice["fg"])

			# packs and adds to the list of entries
			newTask.pack(side=tk.TOP, fill=tk.X)
			self.tasks.append(newTask)

		self.taskCreate.delete(1.0, tk.END) # clears the text box


# if this program is ran (not imported) do this
print(__name__)
if __name__ == "__main__":
	todo = Todo() # store ui in todo
	todo.mainloop() # display the window