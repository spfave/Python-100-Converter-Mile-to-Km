import tkinter as tk


# Functions
def convert_mile_to_km(miles):
    """ Convert input miles to kilometers and return """
    kilometers = round(miles*1.609344, 1)
    return kilometers


# Main
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)


window.mainloop()
