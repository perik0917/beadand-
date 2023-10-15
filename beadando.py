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
        label_vezeteknev = ttk.Label(self.parent, text="Vezetéknév:")
        label_vezeteknev.grid(row=0, column=0, sticky="w")
        self.entry_vezeteknev = ttk.Entry(self.parent)
        self.entry_vezeteknev.grid(row=0, column=1)

        label_keresztnev = ttk.Label(self.parent, text="Keresztnév:")
        label_keresztnev.grid(row=1, column=0, sticky="w")
        self.entry_keresztnev = ttk.Entry(self.parent)
        self.entry_keresztnev.grid(row=1, column=1)

        label_szuletesi_ido = ttk.Label(self.parent, text="Születési idő:")
        (label_szuletesi_ido.grid(row=2, column=0, sticky="w"))

        self.entry_szuletesi_ido = ttk.Entry(self.parent)
        self.entry_szuletesi_ido.grid(row=2, column=1)

        calendar_button = ttk.Button(self.parent, text="Választás", command=self.select_date)
        calendar_button.grid(row=3, column=0, columnspan=2)

        label_szuletesi_hely = ttk.Label(self.parent, text="Születési hely:")
        label_szuletesi_hely.grid(row=4, column=0, sticky="w")
        self.entry_szuletesi_hely = ttk.Entry(self.parent)
        self.entry_szuletesi_hely.grid(row=4, column=1)

        label_cim = ttk.Label(self.parent, text="Lakcím:")
        label_cim.grid(row=5, column=0, sticky="w")

        label_lakohely = ttk.Label(self.parent, text="Lakóhely:")
        label_lakohely.grid(row=6, column=0, sticky="w")
        self.entry_lakohely = ttk.Entry(self.parent)
        self.entry_lakohely.grid(row=6, column=1)

        label_utca = ttk.Label(self.parent, text="Utca:")
        label_utca.grid(row=7, column=0, sticky="w")
        self.entry_utca = ttk.Entry(self.parent)
        self.entry_utca.grid(row=7, column=1)

        label_hazszam = ttk.Label(self.parent, text="Házszám:")
        label_hazszam.grid(row=8, column=0, sticky="w")
        self.entry_hazszam = ttk.Entry(self.parent)
        self.entry_hazszam.grid(row=8, column=1)

        label_taj = ttk.Label(self.parent, text="TAJ-szám (000-000-000):")
        label_taj.grid(row=9, column=0, sticky="w")
        self.entry_taj = ttk.Entry(self.parent)
        self.entry_taj.grid(row=9, column=1)

        regisztracio_button = ttk.Button(self.parent, text="Regisztráció", command=self.register)
        regisztracio_button.grid(row=10, column=0, columnspan=2)

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
            self.entry_szuletesi_ido.delete(0, tk.END)
            self.entry_szuletesi_ido.insert(0, self.selected_date.strftime('%Y-%m-%d'))
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen dátum!")

    def register(self):
        first_name = self.entry_vezeteknev.get()
        last_name = self.entry_keresztnev.get()
        birthdate = self.entry_szuletesi_ido.get()
        birthplace = self.entry_szuletesi_hely.get()
        city = self.entry_lakohely.get()
        street = self.entry_utca.get()
        house_number = self.entry_hazszam.get()
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

# innen indul a program
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationProgram(root)
    root.mainloop()
