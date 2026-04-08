import anvil.files
import sqlite3
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def kursuebersichtfuellen():
  conn = sqlite3.connect(data_files["Zengin_Talha_fitnessstudio.db"])
  cursor = conn.cursor()

  cursor.execute("""
  SELECT 
      k.Bezeichnung AS kurs,
      k.Wochentag AS wochentag,
      k.Uhrzeit AS uhrzeit,
      (t.Vorname || ' ' || t.Nachname) AS trainer,
      (COUNT(b.BuchungID) || "/15") AS teilnehmer
  FROM Kurs AS k
    LEFT JOIN Trainer AS t ON k.TrainerID = t.TrainerID
    LEFT JOIN Buchung AS b ON k.KursID = b.KursID
    GROUP BY k.KursID
    ORDER BY k.Bezeichnung ASC;
  """)

  return_value = cursor.fetchall()
  conn.close()

  return return_value

@anvil.server.callable
def mitgliederbefuellen():
  conn = sqlite3.connect(data_files["Zengin_Talha_fitnessstudio.db"])
  cursor = conn.cursor()

  cursor.execute("""
  SELECT 
      (Vorname || " " || Nachname) AS mitglied
      FROM Mitglied
  """)

  return_value = cursor.fetchall()
  conn.close()
  
  return return_value
