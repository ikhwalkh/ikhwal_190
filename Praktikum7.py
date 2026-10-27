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
