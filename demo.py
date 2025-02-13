from science_jubilee.Machine import Machine
from science_jubilee.tools import Pipette
from science_jubilee.tools import RDE
from science_jubilee.decks import Deck
import time

m = Machine(address='127.0.0.1')                 # a new machine, called 'm'

P300 = Pipette.Pipette.from_config(0, 'Pipette', 'P300_config.json')
m.load_tool(P300)

rde = RDE.RDE.from_config(1, 'BlueRev RDE','P300_config.json')
m.load_tool(rde)
print(m.tool)  # prints the active tool
print(m.tools) # prints all available tools

m.move_to(x=100, y=50, z=200) # moves to the absolute position (100, 50, 200)
m.move_to(x=75)               # moves to the absolute position (75, 50, 200)
m.move(dz=-50)                # moves -50 in the z direction to (75, 50, 150)
time.sleep(2)

m.pickup_tool(P300)
time.sleep(2)
m.park_tool()
time.sleep(2)

m.pickup_tool(1)
time.sleep(2)
m.park_tool()
time.sleep(2)

