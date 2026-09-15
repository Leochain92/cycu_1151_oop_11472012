import tkinter as tk


def show_top_animation():
	window = tk.Tk()
	window.overrideredirect(True)
	window.attributes("-topmost", True)
	window.attributes("-alpha", 0.96)

	width, height = 320, 86
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	x = (screen_width - width) // 2
	y = (screen_height - height) // 2
	window.geometry(f"{width}x{height}+{x}+{y}")

	canvas = tk.Canvas(window, width=width, height=height,
					   bg="#17202a", highlightthickness=0)
	canvas.pack()
	canvas.create_text(width // 2, 30, text="Hello, world!",
					   fill="#f7dc6f", font=("Segoe UI", 20, "bold"))
	canvas.create_text(width // 2, 61, text="點一下關閉動畫",
					   fill="#d5dbdb", font=("Segoe UI", 10))

	dot = canvas.create_oval(18, 12, 30, 24, fill="#5dade2", outline="")
	direction = 1

	def animate():
		nonlocal direction
		canvas.move(dot, 4 * direction, 0)
		dot_x = canvas.coords(dot)[0]
		if dot_x <= 18 or dot_x >= width - 30:
			direction *= -1
		window.after(30, animate)

	window.bind("<Button-1>", lambda event: window.destroy())
	window.after(0, animate)
	window.mainloop()


print("hellow world")
show_top_animation()