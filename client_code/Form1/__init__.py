from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = anvil.server.call('get_direktor', '1')
    self.label_freie_zellen.text = anvil.server.call('get_freiezelle', '1')
    self.repeating_zellen.items = anvil.server.call('get_zelle', '1')
    #[{'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}, 
    #{'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

 



  
 
