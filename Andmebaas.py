import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

global entries

table_languages="""
CREATE TABLE IF NOT EXISTS languages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);"""
insert_into_languages="""
INSERT INTO languages (name) VALUES
(USA),(UK),(Eesti),(Español),(Український),(Русский),(Deutsch),(Français),(Polski),(Italiano),(한국어),(中文)"""
table_countries="""
CREATE TABLE IF NOT EXISTS countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);"""
insert_into_countries="""
INSERT INTO countries (name) VALUES
(English),(Estonia),(Spain),(Ukraine),(Russia),(Germany),(France),(Poland),(Italy),(Korea),(China)"""
table_genre="""
CREATE TABLE IF NOT EXISTS genres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);"""
insert_into_genre="""
INSERT INTO genres (name) VALUES
(Action),(Comedy),(Drama),(Horror),(Science Fiction),(Thriller),(Romance),(Fantasy),(Documentary),(Animation),(Crime),(Adventure)"""
table_director="""
CREATE TABLE IF NOT EXISTS directors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);"""
insert_into_director="""
INSERT INTO directors (name) VALUES
(Francis Ford Coppola),(Christopher Nolan),(Quentin Tarantino),(Steven Spielberg),(Martin Scorsese),(James Cameron),(Ridley Scott),(Alfred Hitchcock),(Greta Gerwig ),(Peter Jackson)"""
create_table="""
CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  director_id INTEGER,
  release_year INTEGER,
  genre_id INTEGER,
  duration INTEGER,
  rating REAL,
  language_id INTEGER,
  country_id INTEGER,
  description TEXT,
  FOREIGN KEY (director_id) REFERENCES directors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id),
  FOREIGN KEY (language_id) REFERENCES languages(id),
  FOREIGN KEY (country_id) REFERENCES countries(id)
);
"""
insert_into="""
INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
('The From In With.', 1, 1994, 3, 142, 9.3, 1, 1, 'The In With By On. A In From By The At. On A With By By On To A.'),

('The By On To.', 2, 2010, 5, 148, 8.8, 1, 2, 'The A The On The In. By To A At On The. From The In With At In To A.'),

('In The With On.', 3, 1972, 11, 175, 9.2, 1, 1, 'On From The By At The A. In From By With To On. A The By In With At On To A.'),

('The A To From.', 4, 1994, 12, 154, 8.9, 1, 7, 'With By In The A On. The With To A At The From. On A From With At By The.'),

('On The From With.', 5, 2008, 1, 152, 9.0, 1, 6, 'The A By On In The. At With To A From On The. With On By The A In To From.'),

('From The By With.', 2, 1960, 3, 134, 8.5, 1, 2, 'The A On From The At. With To By In A The On. At The In From With By To A.'),

('The By On A.', 1, 1999, 6, 112, 7.8, 1, 1, 'A The On By In The At. From With A On By To The. In The By With At A From.'),

('On A The From.', 3, 2015, 2, 126, 7.9, 1, 9, 'By With A On In The From. The By At A With On To. At In The By From With A.'),

('By The On From.', 4, 1975, 1, 143, 8.7, 1, 7, 'A With On The By From In. The A At On With To From. By In The A From With At On.'),

('From With The By.', 5, 1980, 11, 163, 9.1,1, 6, 'On The A By In The From. With By On A The In From. To The In At By With On A.');"""

def create_table():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(create_table)
        print("Tabel loodud")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def table_languages():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(table_languages)
        print("Tabel loodud")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def table_countries():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(table_countries)
        print("Tabel loodud")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def table_genre():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(table_genres)
        print("Tabel loodud")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def table_director():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(table_director)
        print("Tabel loodud")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def täida_tabel():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        cursor.execute(insert_into)
        print("Tabel täidetud")
        conn.commit()
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:
        if conn:
            conn.close()
def loe_tabel(tabel:str):
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Ühendus loodud")

        # Teostame päringu, et lugeda kõik andmed tabelist 'movies'
        cursor.execute("SELECT * FROM {tabel}")
        rows = cursor.fetchall()

        # Väljastame kõik loetud read
        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel või päringu teostamisel:", error)
    finally:
        if conn:
            conn.close()
            print("Ühendus suleti")
def validate_data():
    global entries
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        tk.messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        tk.messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        tk.messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    tk.messagebox.showinfo("Edu", "Andmed on kehtivad!")
    return True
def insert_data():
    global entries
    if validate_data():
        connection = sqlite3.connect("movies.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entries["Pealkiri"].get(),
            entries["Režissöör"].get(),
            entries["Aasta"].get(),
            entries["Žanr"].get(),
            entries["Kestus"].get(),
            entries["Reiting"].get(),
            entries["Keel"].get(),
            entries["Riik"].get(),
            entries["Kirjeldus"].get()
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
        clear_entries()
def clear_entries():
    for entry in entries.values():
        entry.delete(0, tk.END)
    load_data_from_db(tree, search_query="")
def add_language():
    def save():
        global entries
        try:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            language = Entry_languages.get()
            if language:
                cursor.execute("insert or ignore into languages (name) values (?)", (language,))
                conn.commit()
                top.destroy()
        except sqlite3.Error as error:
            print("An error occurred when connecting to the database:", error)
        finally:
            if conn:
                conn.close()
    top = Toplevel(root)
    top.title("Add language")

    Label(top, text="Language:").pack(pady=5)
    Entry_languages = Entry(top)
    Entry_languages.pack(pady=5)
    Button(top, text="Save", command=save).pack(pady=10)
def add_country():
    def save():
        global entries
        try:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            country = Entry_country.get()
            if country:
                cursor.execute("insert or ignore into languages (name) values (?)", (country,))
                conn.commit()
                top.destroy()
        except sqlite3.Error as error:
            print("An error occurred when connecting to the database:", error)
        finally:
            if conn:
                conn.close()
    top = Toplevel(root)
    top.title("Add country")

    Label(top, text="Country:").pack(pady=5)
    Entry_country = Entry(top)
    Entry_country.pack(pady=5)
    Button(top, text="Save", command=save).pack(pady=10)
def add_genre():
    def save():
        global entries
        try:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            genre = Entry_genre.get()
            if genre:
                cursor.execute("insert or ignore into languages (name) values (?)", (genre,))
                conn.commit()
                top.destroy()
        except sqlite3.Error as error:
            print("An error occurred when connecting to the database:", error)
        finally:
            if conn:
                conn.close()
    top = Toplevel(root)
    top.title("Add country")

    Label(top, text="Country:").pack(pady=5)
    Entry_genre = Entry(top)
    Entry_genre.pack(pady=5)
    Button(top, text="Save", command=save).pack(pady=10)
def add_director():
    def save():
        global entries
        try:
            conn = sqlite3.connect('movies.db')
            cursor = conn.cursor()
            director = Entry_director.get()
            if director:
                cursor.execute("insert or ignore into languages (name) values (?)", (director,))
                conn.commit()
                top.destroy()
        except sqlite3.Error as error:
            print("An error occurred when connecting to the database:", error)
        finally:
            if conn:
                conn.close()
    top = Toplevel(root)
    top.title("Add country")

    Label(top, text="Country:").pack(pady=5)
    Entry_director = Entry(top)
    Entry_director.pack(pady=5)
    Button(top, text="Save", command=save).pack(pady=10)


create_table()
täida_tabel()
# loe_tabel("movies")

def lisa_andmed ():
    global entries
    # Loo Tkinteri aken
    root = tk.Tk()
    root.title("Filmi andmete sisestamine")

    # Loo sildid ja sisestusväljad
    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    # Loo nupp andmete sisestamiseks
    submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

    # Näita Tkinteri akent
    root.mainloop()
def load_data_from_db(tree):
    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toomiseks
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")
    rows = cursor.fetchall()

    # Lisa andmed tabelisse
    for row in rows:
        tree.insert("", "end", values=row)

    # Sulge ühendus andmebaasiga
    conn.close()
def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)
# def load_data_from_db(tree, search_query=""):
#     for item in tree.get_children():
#         tree.delete(item)
#     conn = sqlite3.connect('movies.db')
#     cursor = conn.cursor()
#     if search_query:
#         cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE title LIKE ?", ('%' + search_query + '%',))
#     else:
#         cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies")
#     rows = cursor.fetchall()
#     for row in rows:
#         tree.insert("", "end", values=row)
#     conn.close()
def load_data_from_db(tree, search_query=""):
    # Puhasta Treeview tabel enne uute andmete lisamist
    for item in tree.get_children():
        tree.delete(item)

    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toomiseks, koos ID-ga, kuid ID ei kuvata
    if search_query:
        cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE title LIKE ?", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT id, title, director, release_year, genre, duration, rating, language, country, description FROM movies")

    rows = cursor.fetchall()

    # Lisa andmed tabelisse (Treeview), kuid ID-d ei kuvata
    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])  # iid määratakse ID-ks

    # Sulge ühendus andmebaasiga
    conn.close()
def on_update():
    selected_item = tree.selection() 
    if selected_item:
        record_id = selected_item[0]  
        print(f"Valitud ID: {record_id}")
    else:
        print("Vali kõigepealt rida!")
def on_update():
    selected_item = tree.selection() 
    if selected_item:
        record_id = selected_item[0] 
        open_update_window(record_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
def open_update_window(record_id):
    # Loo uus aken
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    # Loo andmebaasi ühendus ja toomine olemasolevad andmed
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE id=?", (record_id,))
    record = cursor.fetchone()
    conn.close()

    # Veergude nimed ja vastavad sisestusväljad
    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(update_window, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, record[i])
        entries[label] = entry

    # Salvestamise nupp
    save_button = tk.Button(update_window, text="Salvesta", command=lambda: update_record(record_id, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
def update_record(record_id, entries, window):
    # Koguge andmed sisestusväljadest
    title = entries["Pealkiri"].get()
    director = entries["Režissöör"].get()
    release_year = entries["Aasta"].get()
    genre = entries["Žanr"].get()
    duration = entries["Kestus"].get()
    rating = entries["Reiting"].get()
    language = entries["Keel"].get()
    country = entries["Riik"].get()
    description = entries["Kirjeldus"].get()

    # Andmete uuendamine andmebaasis
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE movies
        SET title=?, director=?, release_year=?, genre=?, duration=?, rating=?, language=?, country=?, description=?
        WHERE id=?
    """, (title, director, release_year, genre, duration, rating, language, country, description, record_id))
    conn.commit()
    conn.close()

    # Värskenda Treeview tabelit
    load_data_from_db(tree)

    # Sulge muutmise aken
    window.destroy()

    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")
def on_delete():
    selected_item = tree.selection()  # Võta valitud rida
    if selected_item:
        record_id = selected_item[0]  # iid (ID)
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            try:
                # Loo andmebaasi ühendus
                conn = sqlite3.connect('movies.db')
                cursor = conn.cursor()
               
                # Kustuta kirje
                cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
                conn.commit()
                conn.close()
               
                # Värskenda Treeview tabelit
                load_data_from_db(tree)
               
                messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
            except sqlite3.Error as e:
                messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")




root = tk.Tk()
root.title("Filmid")

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

lisa_button=tk.Button(search_frame, text="Lisa Andmeid", command=lisa_andmed)
lisa_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(search_frame, text="Uuenda", command=on_update)
update_button.pack(side=tk.LEFT, padx=10)

lisa_button=tk.Button(search_frame, text="Kustuta", command=on_delete)
lisa_button.pack(side=tk.LEFT, padx=10)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=tree.yview)

tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

load_data_from_db(tree)

root.mainloop()

# # Lisa andmed tabelisse
# # tree.insert("", "end", values=("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 142, 9.3, "English", "USA", "Two imprisoned men bond over a number of years."))
# # tree.insert("", "end", values=("The Godfather", "Francis Ford Coppola", 1972, "Crime, Drama", 175, 9.2, "English", "USA", "The aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant son."))
# # tree.insert("", "end", values=("The Dark Knight", "Christopher Nolan", 2008, "Action, Crime, Drama", 152, 9.0, "English", "USA", "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."))


# # Käivita Tkinteri tsükkel
# root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------