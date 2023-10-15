import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import re

class RegistrationProgram:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Regisztrációs Program")

        # Háttérszín beállítása
        self.parent.configure(bg='#E6F0FF') # világoskék

        self.selected_date = None

        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.day_var = tk.StringVar()

        # Felhasználói felület stílusának beállítása
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 14))  # Gombok méretének növelése
        self.style.configure('TLabel', font=('Helvetica', 14))  # Címkék méretének növelése

        self.create_gui()

    def create_gui(self):
        label_first_name = ttk.Label(self.parent, text="Keresztnév:")
        label_first_name.grid(row=0, column=0, sticky="w")
        self.entry_first_name = ttk.Entry(self.parent)
        self.entry_first_name.grid(row=0, column=1)

        label_last_name = ttk.Label(self.parent, text="Vezetéknév:")
        label_last_name.grid(row=1, column=0, sticky="w")
        self.entry_last_name = ttk.Entry(self.parent)
        self.entry_last_name.grid(row=1, column=1)

        label_birthdate = ttk.Label(self.parent, text="Születési idő:")
        label_birthdate.grid(row=2, column=0, sticky="w")

        self.entry_birthdate = ttk.Entry(self.parent)
        self.entry_birthdate.grid(row=2, column=1)

        calendar_button = ttk.Button(self.parent, text="Választás", command=self.select_date)
        calendar_button.grid(row=3, column=0, columnspan=2)

        label_birthplace = ttk.Label(self.parent, text="Születési hely:")
        label_birthplace.grid(row=4, column=0, sticky="w")
        self.entry_birthplace = ttk.Entry(self.parent)
        self.entry_birthplace.grid(row=4, column=1)

        label_address = ttk.Label(self.parent, text="Lakcím:")
        label_address.grid(row=5, column=0, sticky="w")

        label_city = ttk.Label(self.parent, text="Lakóhely:")
        label_city.grid(row=6, column=0, sticky="w")
        self.entry_city = ttk.Entry(self.parent)
        self.entry_city.grid(row=6, column=1)

        label_street = ttk.Label(self.parent, text="Utca:")
        label_street.grid(row=7, column=0, sticky="w")
        self.entry_street = ttk.Entry(self.parent)
        self.entry_street.grid(row=7, column=1)

        label_house_number = ttk.Label(self.parent, text="Házszám:")
        label_house_number.grid(row=8, column=0, sticky="w")
        self.entry_house_number = ttk.Entry(self.parent)
        self.entry_house_number.grid(row=8, column=1)

        label_taj = ttk.Label(self.parent, text="TAJ-szám (000-000-000):")
        label_taj.grid(row=9, column=0, sticky="w")
        self.entry_taj = ttk.Entry(self.parent)
        self.entry_taj.grid(row=9, column=1)

        register_button = ttk.Button(self.parent, text="Regisztráció", command=self.register)
        register_button.grid(row=10, column=0, columnspan=2)

        self.create_calendar_widgets()

    def create_calendar_widgets(self):
        year_label = ttk.Label(self.parent, text="Év:")
        year_label.grid(row=2, column=2, sticky="w")
        year_entry = ttk.Entry(self.parent, textvariable=self.year_var)
        year_entry.grid(row=2, column=3)

        month_label = ttk.Label(self.parent, text="Hónap:")
        month_label.grid(row=2, column=4, sticky="w")
        month_entry = ttk.Entry(self.parent, textvariable=self.month_var)
        month_entry.grid(row=2, column=5)

        day_label = ttk.Label(self.parent, text="Nap:")
        day_label.grid(row=2, column=6, sticky="w")
        day_entry = ttk.Entry(self.parent, textvariable=self.day_var)
        day_entry.grid(row=2, column=7)

    def select_date(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            self.selected_date = datetime(year, month, day)
            self.entry_birthdate.delete(0, tk.END)
            self.entry_birthdate.insert(0, self.selected_date.strftime('%Y-%m-%d'))
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen dátum!")

    def register(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        birthdate = self.entry_birthdate.get()
        birthplace = self.entry_birthplace.get()
        city = self.entry_city.get()
        street = self.entry_street.get()
        house_number = self.entry_house_number.get()
        taj = self.entry_taj.get()

        if not self.validate_taj(taj):
            messagebox.showerror("Hiba", "Érvénytelen TAJ-szám formátum (000-000-000)!")
            return

        if not house_number.isdigit():
            messagebox.showerror("Hiba", "Házszám csak számokat tartalmazhat!")
            return

        registration_data = f"Név: {first_name} {last_name}, Születési dátum: {birthdate}, Születési hely: {birthplace}, Lakcím: {city}, {street} {house_number}, TAJ-szám: {taj}"

        with open("registered_people.txt", "a") as file:
            file.write(registration_data + "\n")

        messagebox.showinfo("Sikeres regisztráció", "Adataid sikeresen regisztrálva.")

    def validate_taj(self, taj):
        # A TAJ-szám ellenőrzése egy reguláris kifejezéssel
        pattern = r"\d{3}-\d{3}-\d{3}"
        return re.match(pattern, taj) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationProgram(root)
    root.mainloop()
