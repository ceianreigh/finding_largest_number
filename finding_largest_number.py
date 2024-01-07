# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statements.

import tkinter as tk
from tkinter import PhotoImage, messagebox


# pseudocode
def find_biggest_number(number_1_entry, number_2_entry, number_3_entry):
    # function to show error if the user entered invalid number
    try:
        number_1 = int(number_1_entry.get())
        number_2 = int(number_2_entry.get())
        number_3 = int(number_3_entry.get())
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid NUMBERS.",
        )
        return

    # find the biggest number
    if number_1 > number_2 and number_1 > number_3:
        biggest_number = number_1
    elif number_2 > number_1 and number_2 > number_3:
        biggest_number = number_2
    elif number_3 > number_1 and number_3 > number_2:
        biggest_number = number_3
    else:
        biggest_number = "none. All numbers are equal."

    # print the biggest number
    messagebox.showinfo(
        "Biggest Number",
        f"The biggest number is {biggest_number}.",
    )

    # clear the inputs
    number_1_entry.delete(0, tk.END)
    number_2_entry.delete(0, tk.END)
    number_3_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Find the Biggest Number")
window.geometry("500x260")
background_image = PhotoImage(
    file="D:/Programming Logic and Design/finding_largest_number/PLD #4.png"
)
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# heading
heading = tk.Label(
    window,
    text="Find the Biggest Number",
    font=("Cooper Black", 20),
)
heading.pack()

# subheading
subheading = tk.Label(
    window,
    text="Finding the biggest number from the 3 numbers entered",
    font=("Arial Bold Italic", 12),
)
subheading.pack()

frame = tk.Frame(window)
frame.pack(pady=10)

# ask user to input 3 numbers
numbers_frame = tk.LabelFrame(frame, text="Enter 3 Numbers")
numbers_frame.grid(row=0, column=0, padx=10, pady=10)

# number 1
number_1_label = tk.Label(numbers_frame, text="Enter Number 1:")
number_1_label.grid(row=0, column=0, padx=10, pady=5)
number_1_entry = tk.Entry(numbers_frame)
number_1_entry.grid(row=1, column=0, padx=10, pady=5)

# number 2
number_2_label = tk.Label(numbers_frame, text="Enter Number 2:")
number_2_label.grid(row=0, column=1, padx=10, pady=5)
number_2_entry = tk.Entry(numbers_frame)
number_2_entry.grid(row=1, column=1, padx=10, pady=5)

# number 3
number_3_label = tk.Label(numbers_frame, text="Enter Number 3:")
number_3_label.grid(row=0, column=2, padx=10, pady=5)
number_3_entry = tk.Entry(numbers_frame)
number_3_entry.grid(row=1, column=2, padx=10, pady=5)

# find button
find_button = tk.Button(
    frame,
    text="Find",
    font=("Arial", 10),
    command=lambda: find_biggest_number(number_1_entry, number_2_entry, number_3_entry),
)
find_button.grid(row=1, column=0, padx=10, pady=5, columnspan=3, sticky=tk.W + tk.E)

# exit button
exit_button = tk.Button(
    frame,
    text="Exit",
    font=("Arial", 10),
    command=window.destroy,
)
exit_button.grid(row=2, column=0, padx=10, pady=5, columnspan=3, sticky=tk.W + tk.E)

window.mainloop()
