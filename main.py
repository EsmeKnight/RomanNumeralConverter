from tkinter import *
from converter import Converter

converter = Converter()

# call external func
def call_converter():
    conversion = converter.intToRoman(input_entry.get())
    output_entry.delete(0, END)
    output_entry.insert(0, conversion)


# UI
# window
window = Tk()
window.title("Roman Numeral Converter")
window.config(padx=20, pady=20)
# make window start at size == working session window size
window.geometry("265x110")
window.minsize(width=265, height=110)
window.maxsize(width=265, height=110)

# labels
input_label = Label(window, text="Number:")
input_label.grid(column=0, row=0, sticky=E)

output_label = Label(window, text="Roman numeral:")
output_label.grid(column=0, row=1, sticky=E)

# entries
input_entry = Entry(window, width=21)
input_entry.grid(column=1, row=0, sticky=EW)
# focus input entry
input_entry.focus()

output_entry = Entry(window, width=21)
output_entry.grid(column=1, row=1, sticky=EW)


# buttons
convert_button = Button(window, text="Convert", width=17, command=call_converter)
convert_button.grid(column=0, row=2, columnspan=2, sticky=EW)

# functions as a while loop to keep window open
window.mainloop()
