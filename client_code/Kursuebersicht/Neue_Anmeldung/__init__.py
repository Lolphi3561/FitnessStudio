from ._anvil_designer import Neue_AnmeldungTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Neue_Anmeldung(Neue_AnmeldungTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.tabelle_fuellen()

    # Any code you write here will run before the form opens.
  def tabelle_fuellen(self):
    return_value = anvil.server.call("mitgliederbefuellen")

    items = []
    for row in return_value:
      items.append({
        'mitglied': row[0],
      })

    self.repeating_panel_1.items = items
  

  @handle("outlined_button_1", "click")
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Kursuebersicht")
