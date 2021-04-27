import tkinter as tk


def add(nb, color):
	if nb%2 == 1:
		return 0
	print(color)
	temp_frame = tk.LabelFrame(frame, bg=color, text=str(nb))
	temp_frame.grid(row=nb//2, column=nb%2, sticky="nesw")
	label = tk.Label(temp_frame, text=str(nb))
	label.pack()



color = ["red", "green", "blue", "pink"]
fenetre = tk.Tk()
fenetre.geometry("300x300")
frame = tk.LabelFrame(fenetre, bg="brown")
#frame.pack_propagate(False)
frame.pack(expand=True, fill="both")

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
for a in range(0, 4):
	add(a, color[a])








tk.mainloop()

