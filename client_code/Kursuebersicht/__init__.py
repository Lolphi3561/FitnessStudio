from ._anvil_designer import KursuebersichtTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Kursuebersicht(KursuebersichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.tabelle_fuellen()

    # Any code you write here will run before the form opens.
  def tabelle_fuellen(self):
    return_value = anvil.server.call("kursuebersichtfuellen")

    items = []
    for row in return_value:
      items.append({
        'kurs': row[0],
        'wochentag': row[1],
        'uhrzeit': row[2],
        'trainer': row[3],
        'teilnehmer': row[4]
      })

    self.repeating_panel_1.items = items


    
