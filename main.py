import tkinter as tk


# Constants
COL0_WIDTH = 10
COL1_WIDTH = 15
COL2_WIDTH = 10

# Variables
kilometers = 0


# Functions
def convert_mile_to_km(miles):
    """ Convert input miles to kilometers and return """
    kilometers = round(miles*1.609344, 1)
    return kilometers


def button_click():
    """ Get mileage entry and convert to kilometers """
    miles = float(input_miles.get())
    kilometers = convert_mile_to_km(miles)
    label_km_calc.config(text=str(kilometers))


# Main
window = tk.Tk()
window.title("Mile to Km Converter")
window.geometry("300x100")
window.minsize(width=300, height=100)

frame = tk.Frame(window)
frame.place(anchor="center", relx=.5, rely=.5)


# Entry
input_miles = tk.Entry(frame, justify="center", width=COL1_WIDTH)
input_miles.focus()
input_miles.grid(row=0, column=1)


# Labels
label_miles = tk.Label(frame, text="Miles", anchor="w", width=COL2_WIDTH)
label_miles.grid(row=0, column=2)

label_conv_equal = tk.Label(
    frame, text="is equal to", anchor="e", width=COL0_WIDTH)
label_conv_equal.grid(row=1, column=0)

label_km_calc = tk.Label(frame, text=kilometers)
label_km_calc.grid(row=1, column=1)

label_km = tk.Label(frame, text="Kilometers", anchor="w", width=COL2_WIDTH)
label_km.grid(row=1, column=2)


# Button
button_convert = tk.Button(frame, text="Convert",
                           width=COL1_WIDTH, command=button_click)
button_convert.grid(row=2, column=1)

window.mainloop()
