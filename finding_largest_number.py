# Assignment 4
# Ask user to input 3 numbers. Find and print the biggest number using only if-else statements.

import tkinter as tk
from tkinter import PhotoImage, messagebox

# pseudocode
window = tk.Tk()
window.title("Find the Biggest Number")
window.geometry("500x300")

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

# Ask user to input 3 numbers
# Number 1
number_1_frame = tk.Frame(window)
number_1_frame.pack(side=tk.LEFT, pady=10, padx=10)
number_1_label = tk.Label(number_1_frame, text="Number", font=("Arial", 12))
number_1_label.pack(side=tk.TOP)
number_1_icon_label = tk.Label(number_1_frame, text="1", font=("Times New Roman", 50))
number_1_icon_label.pack(side=tk.TOP)
number_1_entry = tk.Entry(number_1_frame)
number_1_entry.pack(side=tk.TOP)

number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
number_3 = int(input("Enter number 3: "))

# Find the biggest number using if-else statements
if number_1 > number_2 and number_1 > number_3:
    highest_number = number_1
elif number_2 > number_1 and number_2 > number_3:
    highest_number = number_2
elif number_3 > number_1 and number_3 > number_2:
    highest_number = number_3
else:
    highest_number = "none. All numbers are equal."

# Print the biggest number
print("The biggest number is", highest_number)

window.mainloop()
