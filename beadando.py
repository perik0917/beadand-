import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


# Saját osztály definiálása
class MyWindow:
    def __init__(self, root):
        self.root = root
        root.title("Regisztrációs Program")

        # Stílus létrehozása ttk-n keresztül
        style = ttk.Style()
        style.configure("TLabel", padding=5, font=("Helvetica", 12))
        style.configure("TEntry", padding=5, font=("Helvetica", 12))

        # Feliratok és mezők
        label_first_name = ttk.Label(root, text="Keresztnév:")
        label_first_name.grid(row=0, column=0, sticky="w")
        self.entry_first_name = ttk.Entry(root)
        self.entry_first_name.grid(row=0, column=1)

        label_last_name = ttk.Label(root, text="Vezetéknév:")
        label_last_name.grid(row=1, column=0, sticky="w")
        self.entry_last_name = ttk.Entry(root)
        self.entry_last_name.grid(row=1, column=1)

        label_birthdate = ttk.Label(root, text="Születési idő:")
        label_birthdate.grid(row=2, column=0, sticky="w")

        # Naptár widget hozzáadása
        self.cal = Calendar(root, selectmode="day", year=2000, month=1, day=1)  # Alapértelmezett dátum beállítása
        self.cal.grid(row=2, column=1)  # Születési idő mező mellett

        label_birthplace = ttk.Label(root, text="Születési hely:")
        label_birthplace.grid(row=3, column=0, sticky="w")
        self.entry_birthplace = ttk.Entry(root)
        self.entry_birthplace.grid(row=3, column=1)

        # Gomb eseménykezelése
        register_button = ttk.Button(root, text="Regisztráció", command=self.register)
        register_button.grid(row=4, column=0, columnspan=2)

        # Gomb eseménykezelése a naptáron
        self.cal.bind("<<CalendarSelected>>", self.update_birthdate)

    def update_birthdate(self, event):
        selected_date = self.cal.get_date()
        self.entry_birthdate.delete(0, tk.END)  # Töröljük a születési idő mező tartalmát
        self.entry_birthdate.insert(0, selected_date)  # Írjuk be a kiválasztott dátumot

    def register(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        birthdate = self.entry_birthdate.get()
        birthplace = self.entry_birthplace.get()
        result = my_function(first_name, last_name, birthdate, birthplace)
        result_label = ttk.Label(self.root, text=f"Regisztrált adatok: {result}")
        result_label.grid(row=5, column=0, columnspan=2)

# Saját függvény
def my_function(first_name, last_name, birthdate, birthplace):
    return f"Név: {first_name} {last_name}, Születési dátum: {birthdate}, Születési hely: {birthplace}"

# Indítjuk az alkalmazást
if __name__ == "__main__":
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()
