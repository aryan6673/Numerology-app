import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def get_numerology_data():
    return {
        1: {
            "title": "Number 1",
            "personality": "Independent, ambitious, and strong-willed. Natural leaders who are self-reliant and innovative.",
            "strengths": "Determined, confident, and proactive.",
            "weaknesses": "Can be stubborn, impatient, and prone to arrogance.",
            "career_paths": "Entrepreneurship, leadership roles, and positions that require initiative.",
            "lucky_colour": "Red",
            "lucky_gemstone": "Ruby",
        },
        2: {
            "title": "Number 2",
            "personality": "Diplomatic, empathetic, and intuitive. Excellent mediators and team players.",
            "strengths": "Cooperative, nurturing, and peaceful.",
            "weaknesses": "Overly sensitive, indecisive, and dependent on others' approval.",
            "career_paths": "Counseling, teaching, or any collaborative work.",
            "lucky_colour": "Orange",
            "lucky_gemstone": "Moonstone",
        },
        3: {
            "title": "Number 3",
            "personality": "Creative, expressive, and optimistic. They have a flair for communication and the arts.",
            "strengths": "Enthusiastic, social, and imaginative.",
            "weaknesses": "Scattered, superficial, and prone to exaggeration.",
            "career_paths": "Art, writing, public speaking, or entertainment.",
            "lucky_colour": "Yellow",
            "lucky_gemstone": "Citrine",
        },
        4: {
            "title": "Number 4",
            "personality": "Practical, disciplined, and reliable. They are the builders of society.",
            "strengths": "Hardworking, methodical, and dependable.",
            "weaknesses": "Rigid, overly cautious, and resistant to change.",
            "career_paths": "Engineering, architecture, or any structured profession.",
            "lucky_colour": "Green",
            "lucky_gemstone": "Emerald",
        },
        5: {
            "title": "Number 5",
            "personality": "Adventurous, curious, and versatile. They thrive on freedom and variety.",
            "strengths": "Dynamic, adaptable, and quick-witted.",
            "weaknesses": "Restless, impulsive, and commitment-phobic.",
            "career_paths": "Travel, marketing, or anything involving change and excitement.",
            "lucky_colour": "Blue",
            "lucky_gemstone": "Turquoise",
        },
        6: {
            "title": "Number 6",
            "personality": "Caring, responsible, and family-oriented. They are natural caregivers.",
            "strengths": "Compassionate, nurturing, and balanced.",
            "weaknesses": "Overbearing, perfectionist, and prone to self-sacrifice.",
            "career_paths": "Healthcare, social work, or any role that involves helping others.",
            "lucky_colour": "Pink",
            "lucky_gemstone": "Rose Quartz",
        },
        7: {
            "title": "Number 7",
            "personality": "Intellectual, introspective, and spiritual. They seek deeper truths.",
            "strengths": "Analytical, intuitive, and contemplative.",
            "weaknesses": "Aloof, secretive, and overly critical.",
            "career_paths": "Research, science, or philosophy.",
            "lucky_colour": "Purple",
            "lucky_gemstone": "Amethyst",
        },
        8: {
            "title": "Number 8",
            "personality": "Ambitious, authoritative, and disciplined. They excel in management.",
            "strengths": "Efficient, resourceful, and resilient.",
            "weaknesses": "Materialistic, controlling, and inflexible.",
            "career_paths": "Finance, business, or politics.",
            "lucky_colour": "Black",
            "lucky_gemstone": "Onyx",
        },
        9: {
            "title": "Number 9",
            "personality": "Compassionate, idealistic, and generous. They strive to make the world a better place.",
            "strengths": "Empathetic, inspirational, and selfless.",
            "weaknesses": "Naive, overly idealistic, and prone to burnout.",
            "career_paths": "Activism, teaching, or any humanitarian work.",
            "lucky_colour": "White",
            "lucky_gemstone": "Diamond",
        },
    }

def calculate_numerology_number(birthdate):
    total = sum(int(digit) for digit in birthdate if digit.isdigit())
    while total > 9 and total not in {11, 22, 33}:
        total = sum(int(digit) for digit in str(total))
    return total

def show_numerology_result(number):
    data = get_numerology_data()
    info = data.get(number, None)
    if info:
        result_window = ctk.CTkToplevel()
        result_window.title(f"Numerology: {info['title']}")
        result_window.geometry("500x400")

        header = ctk.CTkLabel(result_window, text=info['title'], font=("Helvetica", 18, "bold"), fg_color="light blue", corner_radius=10, padx=10, pady=5)
        header.pack(fill="x", pady=10)

        sections = [
            ("Personality", info['personality']),
            ("Strengths", info['strengths']),
            ("Weaknesses", info['weaknesses']),
            ("Career Paths", info['career_paths']),
            ("Lucky Colour", info['lucky_colour']),
            ("Lucky Gemstone", info['lucky_gemstone']),
        ]

        for section, content in sections:
            frame = ctk.CTkFrame(result_window, corner_radius=10, border_color="light blue", border_width=2)
            frame.pack(fill="x", padx=10, pady=5)

            section_title = ctk.CTkLabel(frame, text=section, font=("Helvetica", 14, "bold"), justify="left")
            section_title.pack(anchor="w", padx=10, pady=2)

            section_content = ctk.CTkLabel(frame, text=content, font=("Helvetica", 12), justify="left", wraplength=450)
            section_content.pack(anchor="w", padx=10, pady=2)
    else:
        messagebox.showerror("Error", "Details for this number are not available.")

def on_submit(event=None):
    birthdate = entry.get()
    try:
        datetime.strptime(birthdate, "%Y-%m-%d")
        numerology_number = calculate_numerology_number(birthdate)
        show_numerology_result(numerology_number)
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid date format. Please use YYYY-MM-DD.")

app = ctk.CTk()
app.title("Numerology App")
app.geometry("400x200")

header = ctk.CTkLabel(app, text="Numerology App", font=("Helvetica", 18, "bold"), fg_color="light blue", corner_radius=10, pady=10)
header.pack(fill="x")

frame = ctk.CTkFrame(app, corner_radius=10, fg_color="light yellow", border_color="light blue", border_width=2)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="Enter your birthdate (YYYY-MM-DD):", font=("Helvetica", 12))
label.pack(pady=10)

entry = ctk.CTkEntry(frame, font=("Helvetica", 12), justify="center")
entry.pack(pady=5)
entry.bind("<Return>", on_submit)

submit_button = ctk.CTkButton(frame, text="Submit", command=on_submit, font=("Helvetica", 12), fg_color="light green", hover_color="light blue", corner_radius=10, border_color="light blue", border_width=2)
submit_button.pack(pady=10)

app.mainloop()
