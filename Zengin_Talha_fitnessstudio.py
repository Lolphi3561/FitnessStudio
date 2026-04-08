import sqlite3

conn = sqlite3.connect("Zengin_Talha_fitnessstudio.db")
cursor = conn.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Trainer (
        TrainerID   INTEGER PRIMARY KEY AUTOINCREMENT,
        Vorname     VARCHAR(30) NOT NULL,
        Nachname    VARCHAR(30) NOT NULL,
        Spezialgebiet TEXT
    );

    CREATE TABLE IF NOT EXISTS Kurs (
        KursID          INTEGER PRIMARY KEY AUTOINCREMENT,
        Bezeichnung     TEXT NOT NULL,
        Wochentag       VARCHAR(15) NOT NULL,
        Uhrzeit         TIME NOT NULL,
        max_Teilnehmer  INTEGER NOT NULL,
        TrainerID       INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Mitglied (
        MitgliedID      INTEGER PRIMARY KEY AUTOINCREMENT,
        Vorname         VARCHAR(30) NOT NULL,
        Nachname        VARCHAR(30) NOT NULL,
        EMail           VARCHAR(50) UNIQUE NOT NULL,
        Beitrittsdatum  DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Buchung (
        BuchungID       INTEGER PRIMARY KEY AUTOINCREMENT,
        Anmeldedatum    DATE NOT NULL,
        KursID          INTEGER NOT NULL,
        MitgliedID      INTEGER NOT NULL
    );
""")



trainers = [
    ('Max', 'Mustermann', 'Yoga & Pilates'),
    ('Sarah', 'Sportlich', 'Crossfit & Krafttraining'),
    ('Ümit', 'Ausdauer', 'Zumba & Cardio')
]
cursor.executemany("INSERT INTO Trainer (Vorname, Nachname, Spezialgebiet) VALUES (?,?,?)", trainers)


kurse = [
    ('Morgen-Yoga', 'Montag', '08:00', 15, 1),
    ('Hardcore Crossfit', 'Mittwoch', '18:30', 10, 2),
    ('Zumba Party', 'Freitag', '17:00', 25, 3),
    ('Rücken-Fit', 'Dienstag', '19:00', 20, 1),
    ('Box-Training', 'Donnerstag', '20:15', 12, 2)
]
cursor.executemany("INSERT INTO Kurs (Bezeichnung, Wochentag, Uhrzeit, max_Teilnehmer, TrainerID) VALUES (?, ?, ?, ?, ?)", kurse)


mitglieder = [
    ('Anna', 'Anfänger', 'anna@web.de', '2024-01-10'),
    ('Bernd', 'Beispiel', 'bernd@gmx.de', '2024-02-15'),
    ('Carla', 'Cardio', 'carla@t-online.de', '2024-03-01'),
    ('Daniel', 'Dampf', 'daniel@web.de', '2024-03-10'),
    ('Elena', 'Eisen', 'elena@gmx.de', '2024-03-12'),
    ('Fabian', 'Fit', 'fabian@t-online.de', '2024-03-15')
]
cursor.executemany("INSERT INTO Mitglied (Vorname, Nachname, EMail, Beitrittsdatum) VALUES (?, ?, ?, ?)", mitglieder)


buchungen = [
    ('2024-03-05', 1, 1),
    ('2024-03-06', 1, 2),
    ('2024-03-07', 2, 3),
    ('2024-03-08', 3, 1),
    ('2024-03-16', 4, 4),
    ('2024-03-16', 4, 5),
    ('2024-03-17', 5, 6),
    ('2024-03-17', 5, 4)
]
cursor.executemany("INSERT INTO Buchung (Anmeldedatum, KursID, MitgliedID) VALUES (?, ?, ?)", buchungen)


conn.commit()
conn.close()