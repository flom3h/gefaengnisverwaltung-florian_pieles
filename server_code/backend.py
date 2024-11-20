import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def verbinde_db():
    conn = sqlite3.connect('gefaengnis.db')
    conn.row_factory = sqlite3.Row
    return conn

@anvil.server.callable
def get_gefaengnisse():
  conn = verbinde_db()
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM Gefaengnis")
  res = [dict(row) for row in cursor.fetchall()]
  conn.close()
  return res

@anvil.server.callable
def get_zelle(gefaengnis_id):
  conn = verbinde_db()
  cursor = conn.cursor()

  cursor.execute("""SELECT Zellennummer, Belegt, Aktuelle_Belegung FROM Zelle WHERE GID = ?""",(gefaengnis_id))
  res = [dict(row) for row in cursor.fetchall()]
  conn.close()
  return res

def get_haeftlinge(zelle_id):
    conn = verbinde_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT H.Name, H.Haftdauer, B.Einzug, B.Auszug
        FROM Haeftling H
        JOIN Bewohntzeit B ON H.HID = B.HID
        WHERE B.ZID = ?""", (zelle_id,))
    res = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return res