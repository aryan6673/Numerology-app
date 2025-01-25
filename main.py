import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_numerology_number(birthdate):
    total = sum(int(digit) for digit in birthdate if digit.isdigit())
    while total > 9 and total not in {11, 22}:
        total = sum(int(digit) for digit in str(total))
    return total

def get_numerology_meaning(number):
    meanings = {
        1: "You are a leader, independent, and ambitious. You have a strong sense of individuality.",
        2: "You are a peacemaker, cooperative, and sensitive. You value relationships and harmony.",
        3: "You are creative, optimistic, and expressive. You bring joy to those around you.",
        4: "You are practical, disciplined, and hardworking. You value stability and order.",
        5: "You are adventurous, curious, and free-spirited. You thrive on change and excitement.",
        6: "You are nurturing, responsible, and compassionate. You prioritize family and community.",
        7: "You are introspective, analytical, and spiritual. You seek deeper truths in life.",
        8: "You are ambitious, determined, and focused on success. You aim for material and personal achievements.",
        9: "You are selfless, humanitarian, and idealistic. You work towards making the world a better place.",
        11: "You are intuitive, visionary, and inspiring. You are driven by higher ideals.",
        22: "You are a master builder, practical yet ambitious. You can turn dreams into reality."
    }
    return meanings.get(number, "Unknown numerology number.")

def on_submit():
    birthdate = entry.get()
    try:
        datetime.strptime(birthdate, "%Y-%m-%d")
        numerology_number = calculate_numerology_number(birthdate)
        meaning = get_numerology_meaning(numerology_number)
        messagebox.showinfo("Numerology Result", f"Your numerology number is {numerology_number}.\n\nMeaning: {meaning}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid date format. Please use YYYY-MM-DD.")

# Create the main application window
app = tk.Tk()
app.title("Numerology App")
app.geometry("400x200")
app.configure(bg="white")

# Create and place widgets
label = tk.Label(app, text="Enter your birthdate (YYYY-MM-DD):", bg="white", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(app, font=("Helvetica", 12), justify="center")
entry.pack(pady=5)

submit_button = tk.Button(app, text="Submit", command=on_submit, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
submit_button.pack(pady=10)

# Run the application
app.mainloop()
