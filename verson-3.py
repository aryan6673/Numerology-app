import customtkinter as ctk
import datetime
import time
import threading
from tkinter import messagebox

# Configure appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class NumerologyProApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("🔮 Numerology Pro 2.0")
        self.geometry("800x900")
        self.configure(fg_color="#FFF0F5")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        
        # Numerology data
        self.load_resources()
        self.history = []
        
        # Create widgets
        self.create_widgets()
        
    def load_resources(self):
        """Load numerology meanings and aspect details."""
        self.aspects = {
            'life_path': {
                'title': "Life Path Number 🌟",
                'color': "#FF69B4",
                'icon': "🌟"
            },
            'destiny': {
                'title': "Destiny Number 🎯",
                'color': "#4B0082",
                'icon': "🎯"
            },
            'soul': {
                'title': "Soul Urge Number 💖",
                'color': "#FF4500",
                'icon': "💖"
            },
            'personality': {
                'title': "Personality Number 🦄",
                'color': "#00BFFF",
                'icon': "🦄"
            },
            'birthday': {
                'title': "Birthday Number 🎂",
                'color': "#32CD32",
                'icon': "🎂"
            }
        }
        
        self.meanings = {
            'life_path': {
                "1": "Natural leader, independent, pioneering",
                "2": "Cooperative, diplomatic, intuitive",
                "3": "Creative, expressive, optimistic",
                "4": "Practical, disciplined, hard-working",
                "5": "Adventurous, freedom-loving, adaptable",
                "6": "Nurturing, responsible, community-focused",
                "7": "Analytical, truth-seeking, spiritual",
                "8": "Ambitious, business-minded, powerful",
                "9": "Humanitarian, compassionate, artistic",
                "11": "Intuitive, inspirational, idealistic",
                "22": "Master builder, practical visionary",
                "33": "Master teacher, spiritual guide",
                "0": "Invalid input - please check your name"
            },
            'destiny': {
                "1": "Leadership, independence, and innovation",
                "2": "Cooperation, harmony, and diplomacy",
                "3": "Creativity, self-expression, and joy",
                "4": "Stability, hard work, and practicality",
                "5": "Freedom, adventure, and versatility",
                "6": "Responsibility, nurturing, and balance",
                "7": "Introspection, spirituality, and wisdom",
                "8": "Ambition, success, and material wealth",
                "9": "Humanitarianism, compassion, and idealism",
                "11": "Inspiration, intuition, and spiritual insight",
                "22": "Mastery, large-scale projects, and practical vision",
                "33": "Spiritual guidance, healing, and universal love"
            },
            'soul': {
                "1": "Desire for independence and leadership",
                "2": "Desire for harmony and partnership",
                "3": "Desire for creativity and self-expression",
                "4": "Desire for stability and security",
                "5": "Desire for freedom and adventure",
                "6": "Desire for love and nurturing",
                "7": "Desire for knowledge and spiritual growth",
                "8": "Desire for success and material abundance",
                "9": "Desire to serve humanity and make a difference",
                "11": "Desire for spiritual enlightenment and inspiration",
                "22": "Desire to achieve large-scale goals and make a lasting impact",
                "33": "Desire to heal and uplift humanity through love"
            },
            'personality': {
                "1": "Confident first impression",
                "2": "Warm and approachable demeanor",
                "3": "Friendly and creative personality",
                "4": "Serious and practical appearance",
                "5": "Adventurous and energetic vibe",
                "6": "Caring and responsible nature",
                "7": "Mysterious and intellectual aura",
                "8": "Powerful and authoritative presence",
                "9": "Compassionate and idealistic image"
            },
            'birthday': {
                "1": "Natural leader with strong willpower",
                "2": "Peacemaker with great sensitivity",
                "3": "Creative communicator and optimist",
                "4": "Practical builder with strong values",
                "5": "Freedom-loving adventurer",
                "6": "Nurturing caregiver and problem-solver",
                "7": "Analytical thinker and truth-seeker",
                "8": "Ambitious achiever with business acumen",
                "9": "Compassionate humanitarian",
                "11": "Inspirational visionary with heightened intuition",
                "22": "Master architect of large-scale projects",
                "33": "Spiritual guide focused on universal love"
            }
        }
        
    def create_widgets(self):
        """Create all GUI widgets."""
        # Header
        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.grid(row=0, column=0, pady=20)
        
        self.title_label = ctk.CTkLabel(self.header, 
                                      text="Numerology Pro 2.0 🔮",
                                      font=("Arial Rounded MT Bold", 28),
                                      text_color="#4B0082")
        self.title_label.grid(row=0, column=0, pady=10)
        
        # Input Section
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.grid(row=1, column=0, pady=20)
        
        # Name Entry
        self.name_entry = ctk.CTkEntry(input_frame,
                                     placeholder_text="Full Name",
                                     width=300,
                                     height=40,
                                     font=("Arial", 14),
                                     border_color="#FFB6C1")
        self.name_entry.grid(row=0, column=0, padx=10, pady=10)
        
        # Date Entry
        self.date_entry = ctk.CTkEntry(input_frame,
                                     placeholder_text="DD/MM/YYYY",
                                     width=300,
                                     height=40,
                                     font=("Arial", 14),
                                     border_color="#FFB6C1")
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Calculate Button
        self.calculate_btn = ctk.CTkButton(input_frame,
                                         text="Analyze My Numerology 🌈",
                                         command=self.start_calculation,
                                         width=200,
                                         height=40,
                                         fg_color="#9370DB",
                                         hover_color="#663399",
                                         font=("Arial", 14, "bold"))
        self.calculate_btn.grid(row=1, column=0, columnspan=2, pady=20)
        
        # Loading Animation
        self.loading_label = ctk.CTkLabel(input_frame, text="", font=("Arial", 14))
        self.loading_label.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results Notebook
        self.tabs = ctk.CTkTabview(self, width=700, height=500,
                                 fg_color="#FFFFFF", segmented_button_selected_color="#FF69B4")
        self.tabs.grid(row=2, column=0, pady=20)
        
        for aspect in self.aspects:
            self.tabs.add(self.aspects[aspect]['title'])
            self.create_aspect_tab(aspect)
            
        # History Section
        self.history_frame = ctk.CTkScrollableFrame(self, width=700, height=200,
                                                  fg_color="#FFFFFF")
        self.history_frame.grid(row=3, column=0, pady=20)
        self.history_label = ctk.CTkLabel(self.history_frame, text="Recent Readings 📚",
                                        font=("Arial", 12, "bold"))
        self.history_label.pack(pady=10)
        
    def create_aspect_tab(self, aspect):
        """Create content for each tab."""
        tab = self.tabs.tab(self.aspects[aspect]['title'])
        tab.grid_columnconfigure(0, weight=1)
        
        # Title Label
        title_label = ctk.CTkLabel(tab, 
                                   text=self.aspects[aspect]['title'],
                                   font=("Arial Rounded MT Bold", 20),
                                   text_color=self.aspects[aspect]['color'])
        title_label.grid(row=0, column=0, pady=10)
        
        # Number Label
        number_label = ctk.CTkLabel(tab, 
                                  text="Number: -",
                                  font=("Arial", 18, "bold"),
                                  text_color="#4B0082")
        number_label.grid(row=1, column=0, pady=5)
        
        # Icon Label
        icon_label = ctk.CTkLabel(tab, 
                                  text=self.aspects[aspect]['icon'],
                                  font=("Arial", 24))
        icon_label.grid(row=2, column=0, pady=5)
        
        # Description Label
        description_label = ctk.CTkLabel(tab, 
                                         text="Description will appear here...",
                                         font=("Arial", 14),
                                         wraplength=600)
        description_label.grid(row=3, column=0, pady=10)
        
        # Store the labels for later updates
        setattr(self, f"{aspect}_number_label", number_label)
        setattr(self, f"{aspect}_description_label", description_label)
        
    def start_calculation(self):
        """Start the calculation in a separate thread."""
        self.calculate_btn.configure(state="disabled")
        self.loading_label.configure(text="Calculating... 🔮")
        threading.Thread(target=self.calculate_with_loading).start()
        
    def calculate_with_loading(self):
        """Simulate loading and perform calculation."""
        try:
            # Simulate loading
            for i in range(3):
                self.loading_label.configure(text=f"Calculating{'.'*(i+1)} 🔮")
                time.sleep(0.5)
                
            self.calculate()
        except Exception as e:
            self.show_error(str(e))
        finally:
            self.loading_label.configure(text="")
            self.calculate_btn.configure(state="normal")
            
    def calculate(self):
        """Perform numerology calculations."""
        name = self.name_entry.get().strip()
        date_str = self.date_entry.get().strip()
        
        if not name or not date_str:
            self.show_error("Please fill in both name and date fields")
            return
            
        try:
            # Parse the date
            birth_date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            
            # Validate name contains letters
            if not any(c.isalpha() for c in name):
                self.show_error("Name must contain at least one letter")
                return
            
            # Calculate numerology numbers
            life_path_number = self.calculate_life_path(birth_date)
            destiny_number = self.calculate_destiny(name)
            soul_number = self.calculate_soul(name)
            personality_number = self.calculate_personality(name)
            birthday_number = self.calculate_birthday(birth_date)
            
            # Update the UI with numbers and descriptions
            self.update_result('life_path', life_path_number)
            self.update_result('destiny', destiny_number)
            self.update_result('soul', soul_number)
            self.update_result('personality', personality_number)
            self.update_result('birthday', birthday_number)
            
            # Add to history
            self.history.append(f"{name} - {date_str}")
            self.update_history()
            
        except ValueError as e:
            self.show_error("Invalid date format. Please use DD/MM/YYYY.")
            
    def update_result(self, aspect, number):
        """Update both number and description for an aspect."""
        number_str = str(number)
        getattr(self, f"{aspect}_number_label").configure(text=f"Number: {number_str}")
        
        # Get description with fallback
        description = self.meanings.get(aspect, {}).get(
            number_str, 
            "Meaning not available for this number"
        )
        getattr(self, f"{aspect}_description_label").configure(text=description)
    
    def calculate_life_path(self, birth_date):
        """Calculate the Life Path number."""
        total = birth_date.day + birth_date.month + birth_date.year
        while total > 9 and total not in [11, 22, 33]:
            total = sum(map(int, str(total)))
        return total
    
    def calculate_destiny(self, name):
        """Calculate the Destiny number."""
        name = name.replace(" ", "").lower()
        total = sum(ord(char) - 96 for char in name if char.isalpha())
        if total == 0:
            return 0
        while total > 9 and total not in [11, 22, 33]:
            total = sum(map(int, str(total)))
        return total
    
    def calculate_soul(self, name):
        """Calculate the Soul Urge number."""
        vowels = [char for char in name.lower() if char in 'aeiou']
        total = sum(ord(char) - 96 for char in vowels)
        if total == 0:
            return 0
        while total > 9 and total not in [11, 22, 33]:
            total = sum(map(int, str(total)))
        return total
    
    def calculate_personality(self, name):
        """Calculate the Personality number."""
        consonants = [char for char in name.lower() if char.isalpha() and char not in 'aeiou']
        total = sum(ord(char) - 96 for char in consonants)
        if total == 0:
            return 0
        while total > 9 and total not in [11, 22, 33]:
            total = sum(map(int, str(total)))
        return total
    
    def calculate_birthday(self, birth_date):
        """Calculate the Birthday number."""
        total = birth_date.day
        while total > 9:
            total = sum(map(int, str(total)))
        return total
    
    def update_history(self):
        """Update the history section."""
        for widget in self.history_frame.winfo_children():
            if widget != self.history_label:
                widget.destroy()
        
        for entry in reversed(self.history[-5:]):  # Show last 5 entries
            entry_label = ctk.CTkLabel(self.history_frame, text=entry, font=("Arial", 12))
            entry_label.pack(pady=5)
    
    def show_error(self, message):
        """Show an error message."""
        messagebox.showerror("Error", message)

# Run the application
if __name__ == "__main__":
    app = NumerologyProApp()
    app.mainloop()
