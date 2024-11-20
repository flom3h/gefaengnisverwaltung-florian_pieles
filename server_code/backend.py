import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_gefaengnisse(rows="*"):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name, GID FROM Gefaengnis"))
  conn.close()
  return res

@anvil.server.callable
def get_direktor(gefaengnis_id):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("""SELECT Direktor FROM Verwaltung WHERE GID = ?""",(gefaengnis_id)))
  print(res)
  conn.close()
  return res

@anvil.server.callable
def get_freiezelle(gefaengnis_id):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("""SELECT Freie_Zellen FROM Verwaltung WHERE GID = ?""",(gefaengnis_id)))
  print(res)
  conn.close()
  return res

@anvil.server.callable
def get_zelle(gefaengnis_id):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("""SELECT Zellennummer, Aktuelle_Belegung FROM Zelle WHERE GID = ?""",(gefaengnis_id)))
  print(res)
  conn.close()
  return res

def get_haeftlinge(zelle_id):
    conn = sqlite3.connect(data_files['gefaengnis.db'])
    cursor = conn.cursor()
    res = list(cursor.execute("""
        SELECT H.Name, H.Haftdauer, B.Einzug, B.Auszug
        FROM Haeftling H
        JOIN Bewohntzeit B ON H.HID = B.HID
        WHERE B.ZID = ?""", (zelle_id)))
    conn.close()
    return res