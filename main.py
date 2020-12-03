import tkinter as tk


# Constants
col0_width = 10
col1_width = 15
col2_width = 10

# Variables
kilometers = 0


# Functions
def convert_mile_to_km(miles):
    """ Convert input miles to kilometers and return """
    kilometers = round(miles*1.609344, 1)
    return kilometers


def button_click():
    """ Get mileage entry and convert to kilometers """
    miles = float(mile_entry.get())
    kilometers = convert_mile_to_km(miles)
    label_km_calc.config(text=str(kilometers))


# Main
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=10, pady=10)

# Mile entry
mile_entry = tk.Entry(width=col1_width)
mile_entry.grid(row=0, column=1)

# Labels
label_miles = tk.Label(text="Miles", anchor="w", width=col2_width)
label_miles.grid(row=0, column=2)

label_conv_equal = tk.Label(text="is equal to", anchor="e", width=col0_width)
label_conv_equal.grid(row=1, column=0)

label_km_calc = tk.Label(text=kilometers)
label_km_calc.grid(row=1, column=1)

label_km = tk.Label(text="Kilometers", anchor="w", width=col2_width)
label_km.grid(row=1, column=2)

# Button
convert_button = tk.Button(
    text="Convert", width=col1_width, command=button_click)
convert_button.grid(row=2, column=1)

window.mainloop()
