
from tkinter import *
import platform

equation = None
gui_windows_size = "370x380"

os = platform.platform().split('-')

if os[0].lower() == 'darwin' and os[1] >= '20':
	gui_windows_size = "370x450"

def press(num):
	global equation

	equation.set( equation.get() + str(num) )

def equalpress():

	try:
		global equation

		total = str(eval(equation.get()))
		equation.set(total)

	except:
		equation.set(" error ")

def clear():
	equation.set("")

def handle_keyboard(event):
	if event.char == '\r':
		equalpress()

# Driver code
if __name__ == "__main__":
	gui = Tk()
	equation = StringVar()

	gui.configure(background="light green")

	gui.title("Kalculator UKK")

	gui.geometry(gui_windows_size)

	gui.bind('<KeyPress>',handle_keyboard)

	expression_field = Entry(gui, textvariable=equation)

	expression_field.grid(columnspan=10, ipadx=125)

	button1 = Button(gui, text=' 1 ', fg='black', bg='white',
					command=lambda: press(1), height=4, width=9)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='white',
					command=lambda: press(2), height=4, width=9)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='white',
					command=lambda: press(3), height=4, width=9)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='white',
					command=lambda: press(4), height=4, width=9)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='white',
					command=lambda: press(5), height=4, width=9)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='white',
					command=lambda: press(6), height=4, width=9)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='white',
					command=lambda: press(7), height=4, width=9)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='white',
					command=lambda: press(8), height=4, width=9)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='white',
					command=lambda: press(9), height=4, width=9)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='white',
					command=lambda: press(0), height=4, width=9)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='white',
				command=lambda: press("+"), height=4, width=9)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='white',
				command=lambda: press("-"), height=4, width=9)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='white',
					command=lambda: press("*"), height=4, width=9)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='white',
					command=lambda: press("/"), height=4, width=9)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='white',
				command=equalpress, height=4, width=9)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='white',
				command=clear, height=4, width=9)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='white',
					command=lambda: press('.'), height=4, width=9)
	Decimal.grid(row=6, column=0)
	# start the GUI
	gui.mainloop()