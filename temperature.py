import tkinter as tk
window = tk.Tk()
window.title("Temp. Converter")
window.geometry("250x200")
window.resizable(width=False, height=False)

# creating the function to calculate 

def fah_to_cel():
    fah = entry_temp.get()
    cel = (5/9)*(float(fah) - 32)
    result["text"] = f"{round(cel, 2)} \N{Degree Celsius}"

frame = tk.Frame(master=window)
entry_temp = tk.Entry(master=frame, width=20)
lebel_temp = tk.Label(master=frame, text="\N{Degree Fahrenheit}")

entry_temp.grid(row=0, column=0, sticky="e")
lebel_temp.grid(row=0, column=1, sticky="w")

# creating button to convert

button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fah_to_cel,
    height=2,
    width=5

)
result = tk.Label(master=window, text="\N{Degree Celsius}")







# setting up the layout 
frame.grid(row=0, column=0, padx=10)
button.grid(row=0, column=1, pady=10)
result.grid(row=1, column=0, padx=10)


window.mainloop()











