# forms.py
import tkinter as tk
from tkinter import ttk, messagebox,filedialog
from database import session, Country, City, Hotel, Tour, Tourist


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Туристические путевки")
        self.geometry("600x400")
        self.frames = {}

        for F in (MainForm, CountriesForm, CitiesForm, HotelsForm, ToursForm, TouristsForm, TourAssignmentForm):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainForm)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Главное меню", font=("Arial", 16)).pack(pady=10)

        buttons = [
            ("Страны", CountriesForm),
            ("Города", CitiesForm),
            ("Отели", HotelsForm),
            ("Путевки", ToursForm),
            ("Туристы", TouristsForm),
            ("Назначить туристов", TourAssignmentForm),
        ]

        for text, form_class in buttons:
            tk.Button(self, text=text, command=lambda f=form_class: parent.show_frame(f)).pack(pady=5)


class BaseForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.back_button = tk.Button(self, text="Назад", command=lambda: parent.show_frame(MainForm))
        self.back_button.pack(anchor="nw", padx=10, pady=10)


# --- Форма: Страны ---
class CountriesForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Страны", font=("Arial", 14)).pack(pady=10)

        self.name_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.selected_id = None

        tk.Label(self, text="Название").pack()
        tk.Entry(self, textvariable=self.name_var).pack()

        tk.Label(self, text="Описание").pack()
        tk.Entry(self, textvariable=self.desc_var).pack()

        self.add_button = tk.Button(self, text="Добавить", command=self.save_country)
        self.add_button.pack(pady=5)

        tk.Button(self, text="Удалить", command=self.delete_country, fg="red").pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)
        self.load_countries()

    def load_countries(self):
        self.listbox.delete(0, tk.END)
        for country in session.query(Country).all():
            self.listbox.insert(tk.END, country.name)

    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            country_name = self.listbox.get(index)
            country = session.query(Country).filter_by(name=country_name).first()
            if country:
                self.selected_id = country.id
                self.name_var.set(country.name)
                self.desc_var.set(country.description)
                self.add_button.config(text="Сохранить изменения")

    def save_country(self):
        name = self.name_var.get().strip()
        desc = self.desc_var.get().strip()
        if not name:
            return
        if self.selected_id:
            country = session.query(Country).get(self.selected_id)
            country.name = name
            country.description = desc
        else:
            country = Country(name=name, description=desc)
            session.add(country)
        session.commit()
        self.reset_form()
        self.load_countries()

    def delete_country(self):
        if self.selected_id:
            country = session.query(Country).get(self.selected_id)
            session.delete(country)
            session.commit()
            self.reset_form()
            self.load_countries()

    def reset_form(self):
        self.name_var.set("")
        self.desc_var.set("")
        self.selected_id = None
        self.add_button.config(text="Добавить")


# --- Форма: Города ---
class CitiesForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Города", font=("Arial", 14)).pack(pady=10)

        self.name_var = tk.StringVar()
        self.country_var = tk.StringVar()
        self.selected_id = None

        tk.Label(self, text="Название").pack()
        tk.Entry(self, textvariable=self.name_var).pack()

        tk.Label(self, text="Страна").pack()
        self.country_combo = ttk.Combobox(self, textvariable=self.country_var)
        self.country_combo.pack()

        self.add_button = tk.Button(self, text="Добавить", command=self.save_city)
        self.add_button.pack(pady=5)

        tk.Button(self, text="Удалить", command=self.delete_city, fg="red").pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)
        self.load_countries()
        self.load_cities()

    def load_countries(self):
        countries = session.query(Country).all()
        self.country_combo['values'] = [c.name for c in countries]
        self.countries_dict = {c.name: c.id for c in countries}

    def load_cities(self):
        self.listbox.delete(0, tk.END)
        cities = session.query(City).all()
        for city in cities:
            country = session.query(Country).get(city.country_id)
            self.listbox.insert(tk.END, f"{city.name} ({country.name})")

    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            item = self.listbox.get(index)
            city_name = item.split(" (")[0]
            city = session.query(City).filter_by(name=city_name).first()
            if city:
                self.selected_id = city.id
                self.name_var.set(city.name)
                country = session.query(Country).get(city.country_id)
                self.country_var.set(country.name)
                self.add_button.config(text="Сохранить изменения")

    def save_city(self):
        name = self.name_var.get().strip()
        country_name = self.country_var.get().strip()
        if not name or not country_name:
            return
        country_id = self.countries_dict[country_name]
        if self.selected_id:
            city = session.query(City).get(self.selected_id)
            city.name = name
            city.country_id = country_id
        else:
            city = City(name=name, country_id=country_id)
            session.add(city)
        session.commit()
        self.reset_form()
        self.load_cities()

    def delete_city(self):
        if self.selected_id:
            city = session.query(City).get(self.selected_id)
            session.delete(city)
            session.commit()
            self.reset_form()
            self.load_cities()

    def reset_form(self):
        self.name_var.set("")
        self.country_var.set("")
        self.selected_id = None
        self.add_button.config(text="Добавить")


# --- Форма: Отели ---
class HotelsForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Отели", font=("Arial", 14)).pack(pady=10)

        self.name_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.selected_id = None

        tk.Label(self, text="Название").pack()
        tk.Entry(self, textvariable=self.name_var).pack()

        tk.Label(self, text="Адрес").pack()
        tk.Entry(self, textvariable=self.address_var).pack()

        tk.Label(self, text="Телефон").pack()
        tk.Entry(self, textvariable=self.phone_var).pack()

        tk.Label(self, text="Город").pack()
        self.city_combo = ttk.Combobox(self, textvariable=self.city_var)
        self.city_combo.pack()

        self.add_button = tk.Button(self, text="Добавить", command=self.save_hotel)
        self.add_button.pack(pady=5)

        tk.Button(self, text="Удалить", command=self.delete_hotel, fg="red").pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)
        self.load_cities()
        self.load_hotels()

    def load_cities(self):
        cities = session.query(City).all()
        self.city_combo['values'] = [f"{city.name}, {session.query(Country).get(city.country_id).name}" for city in cities]
        self.cities_dict = {f"{city.name}, {session.query(Country).get(city.country_id).name}": city.id for city in cities}

    def load_hotels(self):
        self.listbox.delete(0, tk.END)
        hotels = session.query(Hotel).all()
        for hotel in hotels:
            city = session.query(City).get(hotel.city_id)
            country = session.query(Country).get(city.country_id)
            self.listbox.insert(tk.END, f"{hotel.name} ({city.name}, {country.name})")

    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            item = self.listbox.get(index)
            hotel_name = item.split(" (")[0]
            hotel = session.query(Hotel).filter_by(name=hotel_name).first()
            if hotel:
                self.selected_id = hotel.id
                self.name_var.set(hotel.name)
                self.address_var.set(hotel.address)
                self.phone_var.set(hotel.phone)
                city = session.query(City).get(hotel.city_id)
                country = session.query(Country).get(city.country_id)
                self.city_var.set(f"{city.name}, {country.name}")
                self.add_button.config(text="Сохранить изменения")

    def save_hotel(self):
        name = self.name_var.get().strip()
        address = self.address_var.get().strip()
        phone = self.phone_var.get().strip()
        city_name = self.city_var.get().strip()
        if not name or not city_name:
            return
        city_id = self.cities_dict[city_name]
        if self.selected_id:
            hotel = session.query(Hotel).get(self.selected_id)
            hotel.name = name
            hotel.address = address
            hotel.phone = phone
            hotel.city_id = city_id
        else:
            hotel = Hotel(name=name, address=address, phone=phone, city_id=city_id)
            session.add(hotel)
        session.commit()
        self.reset_form()
        self.load_hotels()

    def delete_hotel(self):
        if self.selected_id:
            hotel = session.query(Hotel).get(self.selected_id)
            session.delete(hotel)
            session.commit()
            self.reset_form()
            self.load_hotels()

    def reset_form(self):
        self.name_var.set("")
        self.address_var.set("")
        self.phone_var.set("")
        self.city_var.set("")
        self.selected_id = None
        self.add_button.config(text="Добавить")


# --- Форма: Туристы ---
class TouristsForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Туристы", font=("Arial", 14)).pack(pady=10)

        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.selected_id = None

        tk.Label(self, text="Имя").pack()
        tk.Entry(self, textvariable=self.first_name_var).pack()

        tk.Label(self, text="Фамилия").pack()
        tk.Entry(self, textvariable=self.last_name_var).pack()

        self.add_button = tk.Button(self, text="Добавить", command=self.save_tourist)
        self.add_button.pack(pady=5)

        tk.Button(self, text="Удалить", command=self.delete_tourist, fg="red").pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)
        self.load_tourists()

    def load_tourists(self):
        self.listbox.delete(0, tk.END)
        tourists = session.query(Tourist).all()
        for tourist in tourists:
            self.listbox.insert(tk.END, f"{tourist.first_name} {tourist.last_name}")

    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            full_name = self.listbox.get(index)
            first_name, last_name = full_name.split()
            tourist = session.query(Tourist).filter_by(first_name=first_name, last_name=last_name).first()
            if tourist:
                self.selected_id = tourist.id
                self.first_name_var.set(tourist.first_name)
                self.last_name_var.set(tourist.last_name)
                self.add_button.config(text="Сохранить изменения")

    def save_tourist(self):
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        if not first_name or not last_name:
            return
        if self.selected_id:
            tourist = session.query(Tourist).get(self.selected_id)
            tourist.first_name = first_name
            tourist.last_name = last_name
        else:
            tourist = Tourist(first_name=first_name, last_name=last_name)
            session.add(tourist)
        session.commit()
        self.reset_form()
        self.load_tourists()

    def delete_tourist(self):
        if self.selected_id:
            tourist = session.query(Tourist).get(self.selected_id)
            session.delete(tourist)
            session.commit()
            self.reset_form()
            self.load_tourists()

    def reset_form(self):
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.selected_id = None
        self.add_button.config(text="Добавить")


# --- Форма: Путевки ---
class ToursForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Путевки", font=("Arial", 14)).pack(pady=10)

        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        self.hotel_var = tk.StringVar()
        self.selected_id = None

        tk.Label(self, text="Дата начала (ГГГГ-ММ-ДД)").pack()
        tk.Entry(self, textvariable=self.start_date_var).pack()

        tk.Label(self, text="Дата окончания (ГГГГ-ММ-ДД)").pack()
        tk.Entry(self, textvariable=self.end_date_var).pack()

        tk.Label(self, text="Отели").pack()
        self.hotel_combo = ttk.Combobox(self, textvariable=self.hotel_var)
        self.hotel_combo.pack()

        self.add_button = tk.Button(self, text="Добавить", command=self.save_tour)
        self.add_button.pack(pady=5)

        tk.Button(self, text="Удалить", command=self.delete_tour, fg="red").pack(pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)
        self.load_hotels()
        self.load_tours()

    def load_hotels(self):
        hotels = session.query(Hotel).all()
        self.hotel_combo['values'] = [f"{hotel.name}, {session.query(City).get(hotel.city_id).name}" for hotel in hotels]
        self.hotels_dict = {f"{hotel.name}, {session.query(City).get(hotel.city_id).name}": hotel.id for hotel in hotels}

    def load_tours(self):
        self.listbox.delete(0, tk.END)
        tours = session.query(Tour).all()
        for tour in tours:
            hotel = session.query(Hotel).get(tour.hotel_id)
            city = session.query(City).get(hotel.city_id)
            self.listbox.insert(tk.END, f"С {tour.start_date} по {tour.end_date} — {hotel.name}, {city.name}")

    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            item = self.listbox.get(index)
            start_date = item.split(" ")[1]
            end_date = item.split(" ")[3]
            hotel_name = item.split("—")[1].split(",")[0].strip()
            tour = session.query(Tour).join(Hotel).filter(
                Tour.start_date == start_date,
                Tour.end_date == end_date,
                Hotel.name == hotel_name
            ).first()
            if tour:
                self.selected_id = tour.id
                self.start_date_var.set(tour.start_date)
                self.end_date_var.set(tour.end_date)
                hotel = session.query(Hotel).get(tour.hotel_id)
                city = session.query(City).get(hotel.city_id)
                self.hotel_var.set(f"{hotel.name}, {city.name}")
                self.add_button.config(text="Сохранить изменения")

    def save_tour(self):
        start_date = self.start_date_var.get().strip()
        end_date = self.end_date_var.get().strip()
        hotel_name = self.hotel_var.get().strip()
        if not start_date or not end_date or not hotel_name:
            return
        hotel_id = self.hotels_dict[hotel_name]
        if self.selected_id:
            tour = session.query(Tour).get(self.selected_id)
            tour.start_date = start_date
            tour.end_date = end_date
            tour.hotel_id = hotel_id
        else:
            tour = Tour(start_date=start_date, end_date=end_date, hotel_id=hotel_id)
            session.add(tour)
        session.commit()
        self.reset_form()
        self.load_tours()

    def delete_tour(self):
        if self.selected_id:
            tour = session.query(Tour).get(self.selected_id)
            session.delete(tour)
            session.commit()
            self.reset_form()
            self.load_tours()

    def reset_form(self):
        self.start_date_var.set("")
        self.end_date_var.set("")
        self.hotel_var.set("")
        self.selected_id = None
        self.add_button.config(text="Добавить")


# --- Форма: Назначение туристов к путевкам ---
class TourAssignmentForm(BaseForm):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Назначение туристов к путевке", font=("Arial", 14)).pack(pady=10)

        self.tour_var = tk.StringVar()

        tk.Label(self, text="Выберите путевку").pack()
        self.tour_combo = ttk.Combobox(self, textvariable=self.tour_var)
        self.tour_combo.pack(pady=5)

        tk.Label(self, text="Выберите туристов (множественный выбор)").pack()
        self.tourist_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.tourist_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Добавить туристов к путевке", command=self.assign_tourists).pack(pady=5)

        self.load_tours()
        self.load_tourists()

    def load_tours(self):
        tours = session.query(Tour).all()
        self.tour_combo['values'] = [f"{tour.id}: С {tour.start_date} по {tour.end_date}" for tour in tours]
        self.tours_dict = {f"{tour.id}: С {tour.start_date} по {tour.end_date}": tour.id for tour in tours}

    def load_tourists(self):
        tourists = session.query(Tourist).all()
        for tourist in tourists:
            self.tourist_listbox.insert(tk.END, f"{tourist.id}: {tourist.first_name} {tourist.last_name}")

    def assign_tourists(self):
        tour_text = self.tour_var.get().strip()
        if not tour_text:
            tk.messagebox.showwarning("Ошибка", "Выберите путевку")
            return

        selected_indices = self.tourist_listbox.curselection()
        if not selected_indices:
            tk.messagebox.showwarning("Ошибка", "Выберите хотя бы одного туриста")
            return

        tour_id = self.tours_dict[tour_text]

        tour = session.query(Tour).get(tour_id)

        for idx in selected_indices:
            tourist_id = int(self.tourist_listbox.get(idx).split(':')[0])
            tourist = session.query(Tourist).get(tourist_id)
            if tourist not in tour.tourists:
                tour.tourists.append(tourist)

        session.commit()
        tk.messagebox.showinfo("Успех", "Туристы успешно добавлены к путевке")


if __name__ == "__main__":
    app = App()
    app.mainloop()