import sqlite3
import tkinter as tk
import tkinter.messagebox as msg

def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS nilai_siswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_siswa TEXT NOT NULL,
        biologi INTEGER NOT NULL, 
        fisika INTEGER NOT NULL, 
        Inggris INTEGER NOT NULL, 
        prediksi_fakultas TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_db()

def predict():
    if inggris > biologi AND inggris > fisika:
       return "Bahasa"
    elif biologi > inggris AND biologi > fisika:
       return "kedokteran"
    elif fisika > inggris AND fisika > biologi:
      return "Teknik"
    else :
       return "mending nggak usah sekolah"


# CRUD Functions
def add_nilai_siswa.db(name, age, major):
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
              (name, age, major))
 
def get_students():
    return run_query("SELECT id, name, age, major FROM students ORDER BY name")
 
def update_student(sid, name, age, major):
    run_query("UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?",
              (name, age, major, sid))
 
def delete_student(sid):
    run_query("DELETE FROM students WHERE id = ?", (sid,))


# Build the window 
init_db()
root = tk.Tk()
root.title("nilai_siswa.db")
 
entries = {}
for i, field in enumerate(["Name", "Age", "Major"]):
    tk.Label(root, text=field).grid(row=i, column=0)
    entries[field] = tk.Entry(root, width=30)
    entries[field].grid(row=i, column=1, pady=4)
 
cols = ("id", "name", "age", "major")
tree = ttk.Treeview(root, columns=cols,
                    show="headings")
for c in cols:
    tree.heading(c, text=c.title())
tree.grid(row=4, column=0, columnspan=2)