# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statements.

import tkinter as tk
from tkinter import PhotoImage, messagebox

# pseudocode
window = tk.Tk()
window.title("Find the Biggest Number")
window.geometry("500x250")

# heading
heading = tk.Label(
    window,
    text="Find the Biggest Number",
    font=("Cooper Black", 20),
)
heading.pack(pady=10)

# subheading
subheading = tk.Label(
    window,
    text="Finding the biggest number from the 3 numbers entered",
    font=("Arial Bold Italic", 12),
)
subheading.pack()

frame = tk.Frame(window)
frame.pack()

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
    command=lambda: find_biggest_number(),
)
find_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky=tk.W + tk.E)

# ask user to input 3 numbers
number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
number_3 = int(input("Enter number 3: "))

# find the biggest number using if-else statements
if number_1 > number_2 and number_1 > number_3:
    highest_number = number_1
elif number_2 > number_1 and number_2 > number_3:
    highest_number = number_2
elif number_3 > number_1 and number_3 > number_2:
    highest_number = number_3
else:
    highest_number = "none. All numbers are equal."

# print the biggest number
print("The biggest number is", highest_number)

window.mainloop()
