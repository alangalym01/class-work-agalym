from tkinter import *

class UserInfoApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x600")
        self.root.title("Lab 1")
        self.setup_input_fields()

    def setup_input_fields(self):
        Label(self.root, text="Name").pack()
        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        Label(self.root, text="Age").pack()
        self.age_entry = Entry(self.root)
        self.age_entry.pack()

        self.multilingual_status = BooleanVar()
        Checkbutton(self.root, text="I am multilingual", 
                    variable=self.multilingual_status).pack()

        Button(text="Submit", command=self.handle_input).pack()

    def handle_input(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        is_multilingual = self.multilingual_status.get()

        for widget in self.root.winfo_children():
            widget.destroy()

        self.display_results(name, age, is_multilingual)

    def store_languages(self):
        languages = []
        for entry in self.language_entries:
            lang = entry.get()
            if lang:
                languages.append(lang)

        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.display_languages(languages)

    def display_languages(self, languages):
        Label(self.root, text="Languages you speak:").pack(pady=10)
        
        if languages:
            sorted_languages = sorted(languages)
            lang_listbox = Listbox(self.root, height=len(sorted_languages), width=30)
            lang_listbox.pack(pady=10)
            
            for lang in sorted_languages:
                lang_listbox.insert(END, f"• {lang}")
        else:
            Label(self.root, text="No languages entered.").pack()

    def display_learning_plan(self):
        language = self.new_language_entry.get()

        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Learning plan for {language}: ").pack()

        tips = [
            "Practice 30 minutes daily",
            "Use language learning apps like Duolingo",
            "Watch movies with subtitles",
            "Listen to music in the language",
        ]
        
        tips_listbox = Listbox(self.root, width=50)
        tips_listbox.pack(pady=20)
        
        for tip in tips:
            tips_listbox.insert(END, tip)

    def display_results(self, name, age, is_multilingual):
        Label(self.root, text=f"Hello, {name}!").pack()

        Label(self.root, text=f"You are {age} years old. You are elligible for the following things: ").pack()
        listbox = Listbox(self.root, width=50)
        listbox.pack(pady=20)
        if age < 16:
            listbox.insert(END, "Wait until you turn 16")
        if age >= 16:
            listbox.insert(END, "Driving")
            listbox.insert(END, "Working")
        if age >= 18:
            listbox.insert(END, "Voting")
            listbox.insert(END, "Serving on a jury ")
            listbox.insert(END, "Getting married")
            listbox.insert(END, "Enlisting in the military")
            listbox.insert(END, "Making independent decisions regarding your medical care and contracts")
        if age >= 21:
            listbox.insert(END, "Purchasing and consume alcoholic beverages")
            listbox.insert(END, "Gambling at casinos")
            listbox.insert(END, "Entering establishments that require age 21 for entry, e.g. nightclubs")

        if is_multilingual:
            Label(self.root, text="You've indictated that you're multilingual").pack()
            Label(self.root, text="What languages do you speak? Enter up to 5").pack()

            self.language_entries = []

            for i in range(5):
                entry = Entry(self.root)
                entry.pack()
                self.language_entries.append(entry)

            Button(self.root, text="Submit Languages", command=self.store_languages).pack()
        else:
            Label(self.root, text="What language would you like to learn?").pack()
            self.new_language_entry = Entry(self.root)
            self.new_language_entry.pack()

            Button(self.root, text='Get a learning plan', command=self.display_learning_plan).pack()

    def run(self):
        self.root.mainloop()

app = UserInfoApp()
if __name__ == "__main__":
    app.run()